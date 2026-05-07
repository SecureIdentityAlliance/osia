# Authentic Source Interface Provider - Functional Description

**Version**: 1.0.0  
**Compliance**: ETSI TS 119 478 V1.1.1

---

## 1. Overview

This API implements the Authentic Source Interface Provider (ASIP) specification. It enables trusted verification and retrieval of personal attributes from authentic sources (government registries, official databases) to support the issuance in a digital credentials ecosystem. This API is compliant with ETSI TS 119 478 but contains extensions beyond the core specification.


| Endpoint | HTTP Method | Use | Sources |
|----------|-------------|-----|---------|
| **I1 Discover** | | | | 
| /internationalDiscovery | GET | find uri of I1 Discover interface | Custom |
| /search | GET | Search semantic repository for available attributes | **ETSI** REQ-DIP-5.2.2-01 through 07 |
| /retrieve | GET | Find data service endpoints for specific attributes | **ETSI** REQ-DIP-5.3.2-01, REQ-DIP-5.3.2-02 |
| **I2 Verify** | | | | 
| /verify | POST | Verify attribute values against authentic source without retrieving full data | **ETSI** REQ-ASIP-6.1.1.1-03 through 11 |
| /verify/{deferredResponseId} | GET | Poll for deferred verification results | **Custom** (ETSI doesn't mandate deferred for HTTP) |
| **I3 Retrieve** | | | |
| /retrieve | POST | Retrieve actual attribute values from authentic source | **ETSI** REQ-ASIP-6.1.2.1-02 through 04 |
| /retrieve/{deferredResponseId} | GET | Poll for deferred retrieval results | **Custom** |
| **I4 authorize** | | | |
| /oauth2/authorize | GET | OAuth 2.0 authorization code flow start | **ETSI** REQ-AZSP-6.1.3.1-01 through 04 |
| /oauth2/token | POST | Exchange authorization code for access token | **ETSI** REQ-AZSP-6.1.3.1-01 through 05 |
| /oauth2/register | POST | Dynamic client registration | **ETSI** REQ-AZSP-6.1.3.2-01 |
| **I5 identify** | | | |
| /identify | POST | Find persons by partial attribute matching when exact identifiers unknown | **OSIA-styled** (derived from OSIA POST /v1/identify) |
| /identify/{deferredResponseId} | GET | Poll for deferred identification results | **OSIA-styled** (derived from OSIA GET /v1/identify/{taskID}) |
| /attribute-sets | GET | List available predefined attribute set collections | **OSIA-styled** (derived from OSIA GET /v1/attributes/{attributeSetName}/{identifier}) |
| /attribute-sets/{setId}/attributes | GET | Retrieve all attributes in a set for specified person | **OSIA-styled** (derived from OSIA GET /v1/attributes) |
| /contact/{personId} | GET | Retrieve current contact information (email, phone, address) | **OSIA-styled** (derived from OSIA contactData in AttributeSet) |


### Purpose

- Enable issuers and verifiers to verify attributes against authoritative sources
- Provide privacy-preserving attribute verification (full or partial/fragment-based)
- Support biometric verification

## 2. Interfaces

### 2.1 I1 - Discover Interface

**Purpose**: Public discovery of available attributes and data services.

#### GET /internationalDiscovery

Return the uri of the I1 Discover Interface for a specific country code and return the status of the discover interfaces and the country avaliable in this interface

**Request Parameters**:

| Parameter | Type | Required | Description | Sources |
|-----------|------|----------|-------------|---------|
| country | string (ISO 3166-1 alpha-2) | yes |country code of the targeted country | Custom |

**Request Template**:
```
GET /internationalDiscovery?country=<string>
```

**Response** ('internationalDiscoveryResponse'):
| Parameter | Type | Required | Description | Sources |
|-----------|------|----------|-------------|---------|
| uri | string:uri | yes | Discovery interface for the targeted country | Custom |
| status | string | yes | status of the server value can be up, down | Custom |
| supportedCountry | array of string (ISO 3166-1 alpha-2) | yes | List the country that can be reach trought that uri |

**Response Template**:
```json
{
  "uri" : "<string:uri>",
  "status" : "<string:enum(Up, Down)>",
  "supportedCountry" : ["<string:iso3166-alpha2>"]
}
```
#### GET /search

Searches the semantic repository for available attributes.

**Request Parameters**:

| Parameter | Type | Required | Description | Sources |
|-----------|------|----------|-------------|---------|
| assetType | string (fixed: `attribute`) | Yes | Asset type to search for; must be `attribute` | ETSI REQ-DIP-5.2.2-01, REQ-DIP-5.2.2-02 |
| creator | string | No | Filter results by attribute creator name | ETSI REQ-DIP-5.2.2-03 |
| country | string (ISO 3166-1 alpha-2) | No | Filter results by country code | ETSI REQ-DIP-5.2.2-04 |
| text | string | No | Free-text search across attribute metadata | ETSI REQ-DIP-5.2.2-05 |
| semanticDataSpecification | string:uri | No | Filter by semantic data specification URI | ETSI REQ-DIP-5.2.2-06 |
| schemaMediaType | string | No | Filter by schema media type | ETSI REQ-DIP-5.2.2-07 |

**Request Template**:
```
GET /search?assetType=attribute&country=<string>&text=<string>
```

**Response** (`AttributesSearchResponse`):

| Parameter | Type | Required | Description | Sources |
|-----------|------|----------|-------------|---------|
| attributes | array of AttributeMetadata | Yes | Array of matching attribute objects, which contain
attribute-related metadata. | ETSI REQ-DIP-5.2.3-01, REQ-DIP-5.2.3-02 |

**Attribute**:

| Parameter | Type | Required | Description | Sources |
|-----------|------|----------|-------------|---------|
| attributeIdentifier | string:uri | Yes | Unique URI identifier for the attribute. It shall contain the namespace, the local identifier and the version of the attribute | ETSI REQ-DIP-5.2.3-03 |
| title | array of LocalizedText | No | Localized friendly names for the attribute | ETSI REQ-DIP-5.2.3-04 |
| description | array of LocalizedText | No | Localized descriptions of the attribute | ETSI REQ-DIP-5.2.3-05 |
| creator | string | No | Name of the entity that created the attribute definition | ETSI REQ-DIP-5.2.3-06 |
| country | string (ISO 3166-1 alpha-2) | No | Country code of the attribute creator | ETSI REQ-DIP-5.2.3-07 |
| semanticDataSpecification | string:uri | No | URI of the semantic data specification this attribute conforms to | ETSI REQ-DIP-5.2.3-08 |
| schemaDistribution | array of SchemaDistribution (minimum 1) | Yes | Locations where the attribute schema can be accessed | ETSI REQ-DIP-5.2.3-09 |

**SchemaDistribution**:

| Parameter | Type | Required | Description | Sources |
|-----------|------|----------|-------------|---------|
| accessURL | string:uri | Yes | URL to access the schema definition | ETSI REQ-DIP-5.2.3-10 |
| mediaType | string | Yes | Media type of the schema (e.g., `application/json`) | ETSI REQ-DIP-5.2.3-10 |

**Response Template**:
```json
{
  "attributes": [
    {
      "attributeIdentifier": "<string:uri>",
      "title": [
        { "value": "<string>", "language": "<string:iso639-1>" }
      ],
      "description": [
        { "value": "<string>", "language": "<string:iso639-1>" }
      ],
      "creator": "<string>",
      "country": "<string:iso3166-alpha2>",
      "semanticDataSpecification": "<string:uri>",
      "schemaDistribution": [
        { "accessURL": "<string:uri>", "mediaType": "<string>" }
      ]
    }
  ]
}
```

---

#### GET /retrieve (Discovery)

Finds data service endpoints for specific attributes.

**Request Parameters**:

| Parameter | Type | Required | Description | Sources |
|-----------|------|----------|-------------|---------|
| queryType | string (fixed: `dataServices`) | Yes | Query type; must be `dataServices` | ETSI REQ-DIP-5.3.2-01 |
| attributeIdentifier | string:uri | Yes | Unique URI identifier for the attribute. It shall contain the namespace, the local identifier and the version of the attribute | ETSI REQ-DIP-5.3.2-01 |
| country | string (ISO 3166-1 alpha-2) | No | Filter data services by country code | ETSI REQ-DIP-5.3.2-02 |

This API only contain HTTP-based request so conformsTo isn't present here even if it's mentioned in ETSI as optional.

**Request Template**:
```
GET /retrieve?queryType=dataServices&attributeIdentifier=<string:uri>&country=<string>
```

**Response** (`DataServicesResponse`):

| Parameter | Type | Required | Description | Sources |
|-----------|------|----------|-------------|---------|
| dataServices | array of DataService | Yes | Array of data service endpoints for the requested attribute | ETSI REQ-DIP-5.3.3-01, REQ-DIP-5.3.3-02 |

**DataService**:

| Parameter | Type | Required | Description | Sources |
|-----------|------|----------|-------------|---------|
| attributeIdentifier | string:uri | Yes | Unique URI identifier for the attribute. It shall contain the namespace, the local identifier and the version of the attribute | ETSI REQ-DIP-5.3.3-03 |
| endpointDescription | string:uri | Yes | URL to the API specification (e.g., OpenAPI document) | ETSI REQ-DIP-5.3.3-03 |
| endpointURI | string:uri | Yes | Base URL of the verification/retrieval service | ETSI REQ-DIP-5.3.3-03 |
| provider | Provider | Yes | Legal entity operating this data service | ETSI REQ-DIP-5.3.3-03 |
| country | string (ISO 3166-1 alpha-2) | No | Country where this service operates | ETSI REQ-DIP-5.3.3-04 |

**Response Template**:
```json
{
  "dataServices": [
    {
      "attributeIdentifier": "<string:uri>",
      "endpointDescription": "<string:uri>",
      "endpointURI": "<string:uri>",
      "provider": {
        "legalName" : "<string>",
        "identifiers": [
          {
            "type": "<string:uri>", #describe the type of identifier bellow
            "identifier": "<-->"
          }
        ],
        "establishedByLaw": {
          "legislativeIdentifier": "<string:uri>",
          "legalBasis": "<string>"
        }

      },
      "country": "<string:iso3166-alpha2>"
    }
  ]
}
```

---

### 2.2 I2 - Verify Interface

**Purpose**: Verify attributes against the authentic source without retrieving full data.

#### POST /verify

**Verification Modes**:

1. **Full Attribute Verification** (`attributes` array) — ETSI REQ-ASIP-6.1.1.1-08
    - Verifies complete attribute values
    - Each attribute contains `attributeIdentifier` (URI) and `attributeValue` (JSON object)

2. **Fragment Verification** (`attributeFragments` array) — ETSI REQ-ASIP-6.1.1.1-08-01
    - Privacy-preserving verification using JSONPath expressions
    - Verifies specific fields without revealing full attribute values
    - Example: Verify birth year without revealing exact birthdate

3. **Combined Verification** — both arrays per REQ-ASIP-6.1.1.1-05
    - Both arrays can be provided for comprehensive verification

**Request** (`VerifyRequest`):

| Parameter | Type | Required | Description | Sources |
|-----------|------|----------|-------------|---------|
| attributes | array of VerificationAttribute | Conditional | Complete attributes to verify; required if attributeFragments absent | ETSI REQ-ASIP-6.1.1.1-03, REQ-ASIP-6.1.1.1-05 |
| attributeFragments | array of AttributeFragment | Conditional | Attribute fragments for privacy-preserving verification; required if attributes absent | ETSI REQ-ASIP-6.1.1.1-04, REQ-ASIP-6.1.1.1-05 |
| mandate | Mandate | No | Mandate for delegated access on behalf of another data subject | ETSI REQ-ASIP-6.1.1.1-11 (structure: Custom) |

> **Note**: Per REQ-ASIP-6.1.1.1-05, the request SHALL contain `attributes` OR `attributeFragments` OR both.

**VerificationAttribute**:

| Parameter | Type | Required | Description | Sources |
|-----------|------|----------|-------------|---------|
| attributeIdentifier | string:uri | Yes | URI uniquely identifying the attribute type | ETSI REQ-ASIP-6.1.1.1-06-01 |
| attributeValue | object | Yes | JSON object containing the attribute value to verify | ETSI REQ-ASIP-6.1.1.1-06-02, REQ-ASIP-6.1.1.1-06-02-01 |

**AttributeFragment**:

| Parameter | Type | Required | Description | Sources |
|-----------|------|----------|-------------|---------|
| attributeIdentifier | string:uri | Yes | URI of the parent attribute this fragment belongs to | ETSI REQ-ASIP-6.1.1.1-07-01 |
| location | string:jsonpath | Yes | JSONPath expression specifying the fragment location within the attribute | ETSI REQ-ASIP-6.1.1.1-07-02 |
| value | any | Yes | Expected value at the specified JSONPath location | ETSI REQ-ASIP-6.1.1.1-07-03 |

**Request Template**:
```json
{

  "attributes": [
    {
      "attributeIdentifier": "<string:uri>",
      "attributeValue": "<object>"
    }
  ],
  "attributeFragments": [
    {
      "attributeIdentifier": "<string:uri>",
      "location": "<string:jsonpath>",
      "value": "<any>"
    }
  ],
  "mandate": "<Mandate>"
}
```

---

**Verification Result Values** — Source: ETSI REQ-ASIP-6.1.1.2-04

| Parameter | Type | Required | Description | Sources |
|-----------|------|----------|-------------|---------|
| Match | string:uri | — | Value matches authentic source exactly | ETSI REQ-ASIP-6.1.1.2-04 |
| NoMatch | string:uri | — | Value does not match | ETSI REQ-ASIP-6.1.1.2-04 |
| MatchWithVariation | string:uri | — | Fuzzy match (e.g., name variation); response includes AS value | ETSI REQ-ASIP-6.1.1.2-04, REQ-ASIP-6.1.1.1-10-01 |
| Unknown | string:uri | — | No authentic source data available for comparison | ETSI REQ-ASIP-6.1.1.2-04 |

Full URIs: `http://uri.etsi.org/19478/VerificationResult/{Match|NoMatch|MatchWithVariation|Unknown}`

---

**Response** (`VerifyResponse`):

| Parameter | Type | Required | Description | Sources |
|-----------|------|----------|-------------|---------|
| responseId | string:uuid | Yes | Unique identifier for this response | Custom |
| provider | Provider | Yes | Legal entity operating as the ASIP | ETSI REQ-ASIP-6.1.1.2-07 |
| authenticSource | Provider | Conditional | Authentic source entity, when different from the ASIP | ETSI REQ-ASIP-6.1.1.2-08 |
| attributeVerificationResults | array of AttributeVerificationResult | Conditional | Results for each submitted attribute (present when attributes in request) | ETSI REQ-ASIP-6.1.1.2-02 |
| fragmentVerificationResults | array of FragmentVerificationResult | Conditional | Results for each submitted fragment (present when fragments in request and supported) | ETSI REQ-ASIP-6.1.1.2-05 |
| mandateResult | MandateResult | Conditional | Mandate validation outcome (present when mandate in request and supported) | ETSI REQ-ASIP-6.1.1.2-10, REQ-ASIP-6.1.1.2-11 (structure: Custom) |


**AttributeVerificationResult**:

| Parameter | Type | Required | Description | Sources |
|-----------|------|----------|-------------|---------|
| attributeIdentifier | string:uri | Yes | URI of the attribute that was verified | ETSI REQ-ASIP-6.1.1.2-03 |
| attributeVerificationResult | string:uri (enum) | Yes | Verification outcome URI (Match, NoMatch, MatchWithVariation, Unknown). Field name per ETSI TS 119 478 Annex B official OpenAPI schema. | ETSI REQ-ASIP-6.1.1.2-04 |
| VerificationResult | string | Yes | Describe the value of the resukt, value can be "Match", "NoMatch", MatchWithVariation, Unknown | Custom |
| attributeValue | object | Conditional | Attribute value; present for Match (echoed) and MatchWithVariation (AS value) | ETSI REQ-ASIP-6.1.1.2-04-01 to 04-03 |


**FragmentVerificationResult**:

| Parameter | Type | Required | Description | Sources |
|-----------|------|----------|-------------|---------|
| attributeIdentifier | string:uri | Yes | URI of the parent attribute | ETSI REQ-ASIP-6.1.1.2-05 |
| location | string:jsonpath | Yes | JSONPath expression (same as in the request) | ETSI REQ-ASIP-6.1.1.2-06 |
| fragmentVerificationResult | string:uri (enum) | Yes | Verification outcome URI for the fragment | ETSI REQ-ASIP-6.1.1.2-06 |
| VerificationResult | string | Yes | Describe the value of the resukt, value can be "Match", "NoMatch", MatchWithVariation, Unknown | Custom |
| fragmentValue | any | No | Fragment value from the AS (present for Match/MatchWithVariation) | ETSI REQ-ASIP-6.1.1.2-06 |

**Response Template**:
```json
{
  "responseId": "<string:uuid>",
  "provider": "<Provider>",
  "authenticSource": "<Provider>",
  "attributeVerificationResults": [
    {
      "attributeIdentifier": "<string:uri>",
      "attributeVerificationResult": "<string:uri:enum(Match|NoMatch|MatchWithVariation|Unknown)>",
      "VerificationResult": "<string:enum(Match|NoMatch|MatchWithVariation|Unknown)>",
      "attributeValue": "<object>"
    }
  ],
  "fragmentVerificationResults": [
    {
      "attributeIdentifier": "<string:uri>",
      "location": "<string:jsonpath>",
      "fragmentVerificationResult": "<string:uri:enum(Match|NoMatch|MatchWithVariation|Unknown)>",
      "VerificationResult": "<string:enum(Match|NoMatch|MatchWithVariation|Unknown)>",
      "fragmentValue": "<any>"
    }
  ],
  "mandateResult": "<MandateResult>"
}
```

---

#### GET /verify/{deferredResponseId}

Polls for deferred verification results, view part 6 for detailed processing. **Source**: Custom (ETSI does not mandate deferred responses for HTTP interface)

---

### 2.3 I3 - Retrieve Interface

**Purpose**: Retrieve actual attribute values from the authentic source.

#### POST /retrieve

**Request** (`RetrieveRequest`):

| Parameter | Type | Required | Description | Sources |
|-----------|------|----------|-------------|---------|
| attributeIdentifiers | array of string:uri (min 1) | Yes | URIs of attributes to retrieve from the authentic source | ETSI REQ-ASIP-6.1.2.1-02, REQ-ASIP-6.1.2.1-03 |
| mandate | Mandate | No | Mandate for delegated retrieval on behalf of another data subject | ETSI REQ-ASIP-6.1.2.1-04 (structure: Custom) |

**Request Template**:
```json
{
  "attributeIdentifiers": ["<string:uri>"],
  "mandate": "<Mandate>"
}
```

**Response** (`RetrieveResponse`):

| Parameter | Type | Required | Description | Sources |
|-----------|------|----------|-------------|---------|
| responseId | string:uuid | Yes | Unique identifier for this response | Custom |
| provider | Provider | Yes | Legal entity operating as the ASIP | ETSI REQ-ASIP-6.1.2.2-03 |
| authenticSource | Provider | Conditional | Authentic source entity, when different from the ASIP | ETSI REQ-ASIP-6.1.2.2-04 |
| attributes | array of RetrievedAttribute | Conditional | Retrieved attributes (present on successful retrieval) | ETSI REQ-ASIP-6.1.2.2-02 |
| mandateResult | MandateResult | Conditional | Mandate validation outcome | ETSI REQ-ASIP-6.1.2.2-05 (structure: Custom) |

**RetrievedAttribute**:

| Parameter | Type | Required | Description | Sources |
|-----------|------|----------|-------------|---------|
| attributeIdentifier | string:uri | Yes | URI of the retrieved attribute | ETSI REQ-ASIP-6.1.2.2-02-01 |
| attributeValue | object | Yes | JSON object containing the attribute value from the AS | ETSI REQ-ASIP-6.1.2.2-02-01 |
| stringRetrieveResult | string | yes | Per-attribute outcome: Success or Failure | Custom |


**Retrieve Result URIs**: `http://uri.etsi.org/19478/RetrieveResultTypes/{Success|Failure}`

**Response Template**:
```json
{
  "responseId": "<string:uuid>",
  "provider": "<Provider>",
  "authenticSource": "<Provider>",
  "attributes": [
    {
      "attributeIdentifier": "<string:uri>",
      "attributeValue": "<object>",
      "stringRetrieveResult": "<string:enum(Success|Failure)>"
    }
  ],
  "mandateResult": "<MandateResult>"
}
```

#### GET /retrieve/{deferredResponseId}

Polls for deferred retrieval results, view part 6 for detailed processing. **Source**: Custom

---

### 2.4 I4 - Authorize Interface

**Purpose**: OAuth 2.0 compliant authorization code flow.

#### GET /oauth2/authorize

| Parameter | Type | Required | Description | Sources |
|-----------|------|----------|-------------|---------|
| response_type | string (fixed: `code`) | Yes | OAuth 2.0 response type | ETSI REQ-AZSP-6.1.3.1-01 |
| client_id | string | Yes | Registered client identifier | ETSI REQ-AZSP-6.1.3.1-01 |
| redirect_uri | string:uri | Yes | URI to redirect after authorization | ETSI REQ-AZSP-6.1.3.1-01 |
| scope | string | No | Requested scopes (e.g., `verify`, `retrieve`) | ETSI REQ-AZSP-6.1.3.1-01 |
| state | string | Yes | Opaque value for CSRF protection | ETSI REQ-AZSP-6.1.3.4-01 |
| code_challenge | string | Yes | PKCE code challenge (Base64url-encoded SHA-256 hash) | ETSI REQ-AZSP-6.1.3.1-04 |
| code_challenge_method | string (fixed: `S256`) | Yes | PKCE challenge method; must be S256 | ETSI REQ-AZSP-6.1.3.1-04 |

**Request Template**:
```
GET /oauth2/authorize?response_type=code&client_id=<string>&redirect_uri=<string:uri>&scope=<string>&state=<string>&code_challenge=<string>&code_challenge_method=S256
```

**Response**: HTTP 302 redirect to `redirect_uri` with `code` and `state` parameters.

#### POST /oauth2/token

**Request** (`TokenRequest`):

| Parameter | Type | Required | Description | Sources |
|-----------|------|----------|-------------|---------|
| grant_type | string (fixed: `authorization_code`) | Yes | OAuth 2.0 grant type | ETSI REQ-AZSP-6.1.3.1-01 |
| code | string | Yes | Authorization code received from /authorize | ETSI REQ-AZSP-6.1.3.1-01 |
| redirect_uri | string:uri | Yes | Must match the redirect_uri from the authorization request | ETSI REQ-AZSP-6.1.3.1-01 |
| code_verifier | string | Yes | PKCE code verifier (plain text, hashed to match code_challenge) | ETSI REQ-AZSP-6.1.3.1-04 |
| client_id | string | No | Client identifier (when not using client_assertion) | ETSI REQ-AZSP-6.1.3.1-05 |
| client_assertion_type | string | No | JWT bearer assertion type for client authentication | ETSI REQ-AZSP-6.1.3.1-05 |
| client_assertion | string | No | Signed JWT for client authentication (private_key_jwt method) | ETSI REQ-AZSP-6.1.3.1-05 |

**Request Template**:
```
POST /oauth2/token
Content-Type: application/x-www-form-urlencoded

grant_type=authorization_code&code=<string>&redirect_uri=<string:uri>&code_verifier=<string>&client_id=<string>
```

**Response** (`TokenResponse`):

| Parameter | Type | Required | Description | Sources |
|-----------|------|----------|-------------|---------|
| access_token | string:jwt | Yes | JWT access token containing user PID | ETSI REQ-AZSP-6.1.3.1-08 |
| token_type | string (fixed: `Bearer`) | Yes | Token type; always Bearer | ETSI REQ-AZSP-6.1.3.1-01 |
| expires_in | integer | Yes | Token lifetime in seconds | ETSI REQ-AZSP-6.1.3.1-01 |
| refresh_token | string | No | Refresh token for obtaining new access tokens | ETSI REQ-AZSP-6.1.3.1-01 |
| scope | string | No | Granted scopes (may differ from requested) | ETSI REQ-AZSP-6.1.3.1-01 |

**Response Template**:
```json
{
  "access_token": "<string:jwt>",
  "token_type": "Bearer",
  "expires_in": "<integer>",
  "refresh_token": "<string>",
  "scope": "<string>"
}
```

#### POST /oauth2/register

Dynamic client registration (RFC 7591).

**Request** (`ClientRegistrationRequest`):

| Parameter | Type | Required | Description | Sources |
|-----------|------|----------|-------------|---------|
| redirect_uris | array of string:uri | Yes | Allowed redirect URIs for this client | ETSI REQ-AZSP-6.1.3.2-01 |
| software_statement | string:signed-jwt | Yes | Signed JWT containing client metadata and registry URI | ETSI REQ-AZSP-6.1.3.2-01 |
| scope | string | No | Requested scopes for the client | ETSI REQ-AZSP-6.1.3.2-01 |
| token_endpoint_auth_method | string:enum(tls_client_auth, private_key_jwt) | No | Preferred client authentication method | ETSI REQ-AZSP-6.1.3.1-05 |

**Response** (`ClientRegistrationResponse`):

| Parameter | Type | Required | Description | Sources |
|-----------|------|----------|-------------|---------|
| client_id | string | Yes | Assigned client identifier | ETSI REQ-AZSP-6.1.3.2-01 |
| client_secret | string | No | Client secret (if applicable) | ETSI REQ-AZSP-6.1.3.2-01 |
| redirect_uris | array of string:uri | No | Registered redirect URIs | ETSI REQ-AZSP-6.1.3.2-01 |
| scope | string | No | Granted scopes | ETSI REQ-AZSP-6.1.3.2-01 |

**Request Template**:
```json
{
  "redirect_uris": ["<string:uri>"],
  "software_statement": "<string:signed-jwt>",
  "scope": "<string>",
  "token_endpoint_auth_method": "<string:enum(tls_client_auth|private_key_jwt)>"
}
```

**Response Template**:
```json
{
  "client_id": "<string>",
  "client_secret": "<string>",
  "redirect_uris": ["<string:uri>"],
  "scope": "<string>"
}
```

---

### 2.5 I5 Identify Interface

**Purpose**: Find persons by partial attribute matching when exact identifiers are unknown.  
**Source**: OSIA-styled (derived from OSIA `POST /v1/identify`). Not mandated by ETSI TS 119 478.

#### POST /identify

**Request** (`IdentifyRequest`):

| Parameter | Type | Required | Description | Sources |
|-----------|------|----------|-------------|---------|
| searchAttributes | array of VerificationAttribute (min 1) | Yes | Attributes to search by (partial matching supported) | OSIA-styled (OSIA: attributeSet.biographicData) |
| requestedReturnAttributes | array of string:uri | No | URIs of attributes to return for matched persons | OSIA-styled (OSIA: outputAttributeSetName) |
| maxResults | integer (1–100, default 10) | No | Maximum number of results to return | Custom |
| exactMatchRequired | boolean (default false) | No | Whether all search attributes must match exactly | Custom |
| mandate | Mandate | No | Mandate for delegated identification | Custom |

**Response** (`IdentifyResponse`):

| Parameter | Type | Required | Description | Sources |
|-----------|------|----------|-------------|---------|
| responseId | string:uuid | Yes | Unique identifier for this response | Custom |
| provider | Provider | Yes | Legal entity operating the service | ETSI-styled |
| authenticSource | Provider | No | Authentic source entity when different from provider | ETSI-styled |
| identifiedPersons | array of IdentifiedPerson | Yes | List of persons matching the search criteria | OSIA-styled (OSIA: array of AttributeSet) |
| totalMatches | integer | No | Total matches found (may exceed returned count) | Custom |
| mandateResult | MandateResult | No | Mandate validation outcome | Custom |

**IdentifiedPerson**:

| Parameter | Type | Required | Description | Sources |
|-----------|------|----------|-------------|---------|
| person | PersonIdentificationData | Yes | Identification data of the matched person | OSIA-styled |
| matchConfidence | string:uri (enum: High, Medium, Low) | Yes | Confidence level of the match | Custom |
| returnedAttributes | array of RetrievedAttribute | No | Requested attributes for this person | OSIA-styled |
| contactInformation | ContactInformation | No | Contact data for this person (if requested) | OSIA-styled |
| matchDetails | array of MatchDetail | No | Per-attribute match breakdown | Custom |

**PersonIdentificationData**

| Parameter | Type | Required | Description | Sources |
|-----------|------|----------|-------------|---------|
| familyName | string | Yes | Family name / surname | Custom |
| givenName | string | Yes | Given name / first name | Custom |
| dateOfBirth | string:date | Yes | Date of birth in ISO 8601 format | Custom |
| personIdentifier | string | Yes | Unique person identifier (PID) | Custom |
| placeOfBirth | string | No | Place of birth | Custom |
| currentAddress | string | No | Current residential address | Custom |
| gender | string | No | Gender | Custom |

**MatchDetail**:

| Parameter | Type | Required | Description | Sources |
|-----------|------|----------|-------------|---------|
| attributeIdentifier | string:uri | No | URI of the attribute that was matched | Custom |
| matchedValue | object | No | The value from the AS that was matched against | Custom |
| matchResult | string  | No | How this specific attribute matched, value can be Match or MatchWithVariation | Custom |

**Request Template**:
```json
{
  "searchAttributes": [
    {
      "attributeIdentifier": "<string:uri>",
      "attributeValue": "<object>"
    }
  ],
  "requestedReturnAttributes": ["<string:uri>"],
  "maxResults": "<integer>",
  "exactMatchRequired": "<boolean>",
  "mandate": "<Mandate>"
}
```

**Response Template**:
```json
{
  "responseId": "<string:uuid>",
  "provider": "<Provider>",
  "authenticSource": "<Provider>",
  "identifiedPersons": [
    {
      "person": {
        "familyName": "<string>",
        "givenName": "<string>",
        "dateOfBirth": "<string:date>",
        "personIdentifier": "<string>",
        "placeOfBirth": "<string>",
        "currentAddress": "<string>",
        "gender": "<string>"
      },
      "matchConfidence": "<string:uri:enum(High|Medium|Low)>",
      "returnedAttributes": [
        {
          "attributeIdentifier": "<string:uri>",
          "attributeValue": "<object>",
          "stringRetrieveResult": "<string:enum(Success|Failure)>"
        }
      ],
      "contactInformation": "<ContactInformation>",
      "matchDetails": [
        {
          "attributeIdentifier": "<string:uri>",
          "matchedValue": "<object>",
          "matchResult": "<string:enum(Match|MatchWithVariation)>"
        }
      ]
    }
  ],
  "totalMatches": "<integer>",
  "mandateResult": "<MandateResult>"
}
```

#### GET /identify/{deferredResponseId}

Polls for deferred identification results, view part 6 for detailed processing. **Source**: OSIA-styled (OSIA: `GET /v1/identify/{taskID}`)

#### GET /attribute-sets

Lists available attribute sets.

**Request Parameters**:

| Parameter | Type | Required | Description | Sources |
|-----------|------|----------|-------------|---------|
| country | string (ISO 3166-1 alpha-2) | No | Filter sets by country | ETSI-styled |
| purpose | string:enum | No | Filter by intended purpose | Custom |

**Response** (`AttributeSetsResponse`):

| Parameter | Type | Required | Description | Sources |
|-----------|------|----------|-------------|---------|
| sets | array of AttributeSet | Yes | List of available attribute set definitions | OSIA-styled |

**AttributeSet**:

| Parameter | Type | Required | Description | Sources |
|-----------|------|----------|-------------|---------|
| setId | string | Yes | Unique identifier for this attribute set | Custom (OSIA: attributeSetName) |
| name | array of LocalizedText | Yes | Localized display names | ETSI-styled |
| description | array of LocalizedText | No | Localized descriptions of the set's purpose | ETSI-styled |
| purpose | string:enum(eidas, identity_verification, age_verification, biometric_enrollment, credential_issuance, other) | No | Intended use case for this set | Custom |
| country | string (ISO 3166-1 alpha-2) | No | Country this set is designed for | ETSI-styled |
| attributeIdentifiers | array of string:uri | Yes | URIs of the attributes included in this set | ETSI-styled |
| metadata | object | No | Version and validity period (version, validFrom, validUntil) | Custom |

**Request Template**:
```
GET /attribute-sets?country=<string:iso3166-alpha2>&purpose=<string:enum>
```

**Response Template**:
```json
{
  "sets": [
    {
      "setId": "<string>",
      "name": [
        { "value": "<string>", "language": "<string:iso639-1>" }
      ],
      "description": [
        { "value": "<string>", "language": "<string:iso639-1>" }
      ],
      "purpose": "<string:enum(eidas|identity_verification|age_verification|biometric_enrollment|credential_issuance|other)>",
      "country": "<string:iso3166-alpha2>",
      "attributeIdentifiers": ["<string:uri>"],
      "metadata": {
        "version": "<string>",
        "validFrom": "<string:date-time>",
        "validUntil": "<string:date-time>"
      }
    }
  ]
}
```

#### GET /attribute-sets/{setId}/attributes

Retrieves all attributes in a set for a specified person.

| Parameter | Type | Required | Description | Sources |
|-----------|------|----------|-------------|---------|
| setId | string (path) | Yes | Identifier of the attribute set to retrieve | OSIA-styled |
| personIdentifier | string (query) | Yes | Unique identifier of the person | OSIA-styled |

**Request Template**:
```
GET /attribute-sets/{setId}/attributes?personIdentifier=<string>
```

**Response**: Uses the `RetrieveResponse` schema (see section 2.3).

#### GET /contact/{personId}

Retrieve current contact information (email, phone, address).  

| Parameter | Type | Required | Description | Sources |
|-----------|------|----------|-------------|---------|
| personId | string (path) | Yes | Unique identifier of the person | OSIA-styled |
| preferredOnly | boolean (query) | No | If true, return only preferred/default contact methods | Custom |

**Request Template**:
```
GET /contact/{personId}?preferredOnly=<boolean>
```

**Response** (`ContactResponse`):

| Parameter | Type | Required | Description | Sources |
|-----------|------|----------|-------------|---------|
| responseId | string:uuid | Yes | Unique identifier for this response | Custom |
| issueDateTime | string:date-time | Yes | Timestamp when the response was created | Custom |
| provider | Provider | Yes | Legal entity providing the contact data | ETSI-styled |
| authenticSource | Provider | No | Authentic source when different from provider | ETSI-styled |
| contactInformation | ContactInformation | Yes | Contact data for the person | OSIA-styled (OSIA: contactData) |
| auditTrail | AuditTrail | No | Audit information for data protection compliance | Custom |

**ContactInformation** (OSIA uses dynamic key-value; this uses structured fields):

| Parameter | Type | Required | Description | Sources |
|-----------|------|----------|-------------|---------|
| personId | string | Yes | Reference to the person this contact info belongs to | OSIA-styled |
| emailAddresses | array of EmailAddress | No | Email addresses with preference and purpose | OSIA-styled (OSIA: contactData.email) |
| phoneNumbers | array of PhoneNumber | No | Phone numbers with type and preference | OSIA-styled (OSIA: contactData.phone1, phone2) |
| postalAddress | PostalAddress | No | Current postal/mailing address | Custom |
| preferredContactMethod | string:enum(email, phone, mail, other) | No | Person's preferred way to be contacted | Custom |
| consentStatus | ConsentStatus | No | GDPR/consent status for contacting this person | Custom |

**EmailAddress**:

| Parameter | Type | Required | Description | Sources |
|-----------|------|----------|-------------|---------|
| email | string:email | Yes | Email address | OSIA-styled |
| isPreferred | boolean | No | Whether this is the preferred email | Custom |
| purpose | string:enum(personal, work, other) | No | Usage context of this email | Custom |

**PhoneNumber**:

| Parameter | Type | Required | Description | Sources |
|-----------|------|----------|-------------|---------|
| number | string | Yes | Phone number | OSIA-styled |
| type | string:enum(mobile, home, work, fax, other) | No | Type of phone line | Custom |
| isPreferred | boolean | No | Whether this is the preferred phone number | Custom |
| countryCode | string | No | International dialing code (e.g., "+33") | Custom |

**PostalAddress**:

| Parameter | Type | Required | Description | Sources |
|-----------|------|----------|-------------|---------|
| streetAddress | array of string | No | Street address lines | Custom |
| locality | string | No | City or locality | Custom |
| region | string | No | State, province, or region | Custom |
| postalCode | string | No | Postal/ZIP code | Custom |
| country | string (ISO 3166-1 alpha-2) | No | Country code | Custom |

**ConsentStatus**:

| Parameter | Type | Required | Description | Sources |
|-----------|------|----------|-------------|---------|
| canContact | boolean | No | Whether the person has consented to be contacted | Custom |
| consentDate | string:date-time | No | Date and time consent was given | Custom |
| consentType | string:enum(explicit, implied, none) | No | Type of consent obtained | Custom |

**AuditTrail**:

| Parameter | Type | Required | Description | Sources |
|-----------|------|----------|-------------|---------|
| retrievalReason | string | No | Stated reason for retrieving the contact data | Custom |
| authorizedBy | string | No | Entity/client that authorized the retrieval | Custom |
| authorizationTime | string:date-time | No | Timestamp of the authorization | Custom |

**Response Template**:
```json
{
  "responseId": "<string:uuid>",
  "issueDateTime": "<string:date-time>",
  "provider": "<Provider>",
  "authenticSource": "<Provider>",
  "contactInformation": {
    "personId": "<string>",
    "emailAddresses": [
      { "email": "<string:email>", "isPreferred": "<boolean>", "purpose": "<string:enum>" }
    ],
    "phoneNumbers": [
      { "number": "<string>", "type": "<string:enum>", "isPreferred": "<boolean>", "countryCode": "<string>" }
    ],
    "postalAddress": {
      "streetAddress": ["<string>"], "locality": "<string>", "region": "<string>",
      "postalCode": "<string>", "country": "<string:iso3166-alpha2>"
    },
    "preferredContactMethod": "<string:enum(email|phone|mail|other)>",
    "consentStatus": {
      "canContact": "<boolean>", "consentDate": "<string:date-time>", "consentType": "<string:enum>"
    }
  },
  "auditTrail": {
    "retrievalReason": "<string>", "authorizedBy": "<string>", "authorizationTime": "<string:date-time>"
  }
}
```

---

## 3. Shared Data Models

### 3.1 LocalizedText — Source: ETSI

| Parameter | Type | Required | Description | Sources |
|-----------|------|----------|-------------|---------|
| value | string | Yes | The text content | ETSI REQ-DIP-5.2.3-04 |
| language | string (ISO 639-1) | Yes | Two-letter language code (e.g., `en`, `fr`) | ETSI REQ-DIP-5.2.3-04 |

### 3.2 Provider — Source: ETSI

| Parameter | Type | Required | Description | Sources |
|-----------|------|----------|-------------|---------|
| legalName | string | Yes | Current legal name of the entity | ETSI REQ-DIP-5.3.3-03 |
| identifiers | array of ProviderIdentifier | No | Typed identifiers (e.g., VATIN, national org ID) | ETSI REQ-DIP-5.3.3-03 |
| establishedByLaw | EstablishedByLaw | No | Legal basis for public sector entities | ETSI REQ-DIP-5.3.3-03 |
| currentAddress | string | No | Current address of the entity | ETSI REQ-DIP-5.3.3-03 |

**ProviderIdentifier**:

| Parameter | Type | Required | Description | Sources |
|-----------|------|----------|-------------|---------|
| type | string:uri | Yes | URI identifying the identifier scheme | ETSI REQ-DIP-5.3.3-03 |
| identifier | string | Yes | The identifier value within the scheme | ETSI REQ-DIP-5.3.3-03 |

**EstablishedByLaw**:

| Parameter | Type | Required | Description | Sources |
|-----------|------|----------|-------------|---------|
| legislativeIdentifier | string:uri | No | URI identifying the legislation | ETSI REQ-DIP-5.3.3-03 |
| legalBasis | string | No | Human-readable legal basis description | ETSI REQ-DIP-5.3.3-03 |

### 3.3 Mandate — Source: Custom

> **ETSI TS 119 478**: "The specification of details for the mandate property and its handling by the ASIP is beyond the scope of the present specification." (NOTE 3, clause 6.1.1.1). The structure below requires manual specification.

| Parameter | Type | Required | Description | Sources |
|-----------|------|----------|-------------|---------|
| mandateType | string | Yes | Type of mandate (e.g., LEGAL_REPRESENTATIVE, POWER_OF_ATTORNEY) | Custom |
| mandateReference | string | Yes | Unique reference to the registered mandate | Custom |
| delegator | object | Yes | Person granting authority (personIdentifier, familyName, givenName) | Custom |
| delegate | object | Yes | Person receiving authority (personIdentifier, familyName, givenName) | Custom |
| validFrom | string:date-time | No | Start of mandate validity period | Custom |
| validUntil | string:date-time | No | End of mandate validity period | Custom |
| scope | array of string:uri | No | Attribute URIs covered by this mandate | Custom |

### 3.4 MandateResult — Source: Custom

> ETSI only mandates that `mandateResult` SHALL be present when a mandate was in the request and supported (REQ-ASIP-6.1.1.2-11). The internal structure is not specified.

| Parameter | Type | Required | Description | Sources |
|-----------|------|----------|-------------|---------|
| mandateValid | boolean | Yes | Whether the mandate is valid and active | Custom |
| mandateReference | string | Yes | Reference to the validated mandate | Custom |
| validationTime | string:date-time | No | Timestamp when the mandate was validated | Custom |
| delegatorMatch | boolean | No | Whether the delegator matches the request context | Custom |
| delegateMatch | boolean | No | Whether the delegate matches the authenticated user | Custom |
| validationDetails | object | No | Additional details (mandateStatus: ACTIVE/SUSPENDED/EXPIRED/REVOKED, scopeValid) | Custom |

### 3.5 DeferredResponse — Source: Custom

> ETSI does not define deferred responses for the HTTP/OAuth interface. This structure is a custom addition for asynchronous processing.

| Parameter | Type | Required | Description | Sources |
|-----------|------|----------|-------------|---------|
| responseId | string:uuid | Yes | Identifier for polling the deferred result | Custom |
| status | string (fixed: `deferred`) | Yes | Fixed value indicating async processing | Custom |
| responseAvailableDateTime | string:date-time | Yes | Estimated time when the result will be available | Custom |
| estimatedWaitSeconds | integer | No | Estimated wait time in seconds | Custom |

**Response Template**:
```json
{
  "responseId": "<string:uuid>",
  "status": "deferred",
  "responseAvailableDateTime": "<string:date-time>",
  "estimatedWaitSeconds": "<integer>"
}
```

---

## 4. Security Model

**Source**: ETSI (REQ-AZSP-6.1.3.1-01 through REQ-AZSP-6.1.3.4-02)

| Parameter | Type | Required | Description | Sources |
|-----------|------|----------|-------------|---------|
| Protocol | OAuth 2.0 + FAPI 2.0 | Yes | Authorization framework and security profile | ETSI REQ-AZSP-6.1.3.1-01, REQ-AZSP-6.1.3.4-01 |
| PKCE | S256 | Yes | Proof Key for Code Exchange, mandatory method | ETSI REQ-AZSP-6.1.3.1-04 |
| Client Auth | MTLS or private_key_jwt | Yes | Client authentication mechanism | ETSI REQ-AZSP-6.1.3.1-05 |
| Token Binding | MTLS or DPoP | Yes | Sender-constrained access token mechanism | ETSI REQ-AZSP-6.1.3.1-06 |
| Token Format | JWT (RFC 9068) | Yes | Access token format with user PID | ETSI REQ-AZSP-6.1.3.1-08 |
| Client Registration | Dynamic (RFC 7591) | Yes | Dynamic client registration with signed software statement | ETSI REQ-AZSP-6.1.3.2-01 |

### Scopes

| Parameter | Type | Required | Description | Sources |
|-----------|------|----------|-------------|---------|
| verify | string | — | Access to I2 Verify interface | ETSI |
| retrieve | string | — | Access to I3 Retrieve interface | ETSI |
| identify | string | — | Access to Identify extension | Custom |
| attributeSets | string | — | Access to Attribute Sets extension | Custom |
| contact | string | — | Access to Contact extension | Custom |

### Public Endpoints
I1 Discovery endpoints (`/search`, `/retrieve` GET) require no authentication.

---

## 5. Error Handling

**Source**: ETSI HTTP status codes (REQ-ASIP-6.1.1.2-12, REQ-ASIP-6.1.2.2-06). Error response body is a Custom addition (ETSI only mandates HTTP status codes for the HTTP interface).

### HTTP Status Codes — ETSI & Custom

| Parameter | Type | Required | Description | Sources |
|-----------|------|----------|-------------|---------|
| 200 | HTTP status | — | Request processed successfully; see response body | ETSI REQ-ASIP-6.1.1.2-12 |
| 202 | HTTP status | — | Deferred response; poll for async result | Custom |
| 400 | HTTP status | — | Malformed or invalid request body | ETSI REQ-ASIP-6.1.1.2-12 |
| 401 | HTTP status | — | Authentication or authorization failure | ETSI REQ-ASIP-6.1.1.2-12 |
| 403 | HTTP status | — | Insufficient permissions or consent required | Custom |
| 404 | HTTP status | — | Resource, person, or attribute not found | ETSI REQ-ASIP-6.1.1.2-12 |
| 408 | HTTP status | — | Request timeout | Custom |
| 500 | HTTP status | — | Internal server error | Custom |
| 501 | HTTP status | — | Optional feature not implemented (fragments, mandate) | ETSI REQ-ASIP-6.1.1.1-09, REQ-ASIP-6.1.1.1-13 |
| 503 | HTTP status | — | Service temporarily unavailable | Custom |

---

## 6. Deferred Processing

**Source**: Custom

1. Initial request returns HTTP 202 with `DeferredResponse`
2. Response includes `responseId` for polling
3. Client polls `GET /{operation}/{deferredResponseId}`
4. Returns HTTP 200 when ready, HTTP 202 while pending

---

## 7. Attribute Identification

All attributes use URI-based identification per the specification.

**Example URIs**:
- `urn:etsi:19478:attribute:naturalperson:CurrentFamilyName/v1.0`
- `urn:etsi:19478:attribute:naturalperson:DateOfBirth/v1.0`

Schemas are discoverable via I1 `/search` endpoint with `schemaDistribution` providing access URLs and media types.

---

