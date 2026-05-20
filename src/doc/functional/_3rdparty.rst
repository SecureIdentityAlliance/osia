
Authentic Sources Services
--------------------

Authentic Sources Services consist of a set of services implemented on top of identity systems to favour third parties
consumption of identity data. The services can be classified in four sets:

- Discovery: Public discovery of available attributes and data services

- Verification: Submitting citizen ID attributes for validation

  The purpose is to extend the use of government-issued identity to registered
  third party services. The individual will submit their ID attributes to the third party in order to enroll
  for, or access, a particular service. The third party will leverage the API to access the identity
  management system and verify the individual's identity. In this way, external third parties can quickly and
  easily verify individuals based on their government issued ID attributes.

  .. admonition:: Use case applications: telco enrollment

      The API enables a telco operator to check an individual's identity when he is applying for a service contract.
      The telco relies on the government to confirm that the attributes submitted by the individual match against
      the data held in the database therefore being able to confidently identify the new subscriber. This scenario
      can be replicated across multiple sectors including banking and finance.

- Retrieval: Retrieve actual attribute values from the authentic source 

- Identification: Find persons by partial attribute matching when exact identifiers are unknown

Note: The described Authentic Sources Services are compliant with the eIDAS regulation from a functional standpoint (Ref. ETSI 119 478).

Services
""""""""

.. py:function:: FindAttribute(assetType, creator, country, text, semanticDataSpecification, schemaMediaType)
    :noindex:

    This interface is implemented by a semantic repository which is a catalogue of semantic assets (e.g. attributes, attestation schemes, code lists) enabling the discovery of the unique identifier for a specific attribute and related semantic information and data models. This interface allows to search the semantic repository for attribute-related metadata. 

    **Authorization**: none

    :param str assetType: Asset type to search for; shall be `attribute`
    :param str creator: Represents the name of the creator of the catalogue asset e.g. entity submitting the attribute to the catalogue
    :param str country: Filters results by country code (ISO 3166-1 alpha-2). The country code represents the State of the creator of the catalogue asset
    :param str text: allows a free-text search on the names and descriptions of the catalogued attribute
    :param str semanticDataSpecification:  URI that allows to filter for a specific semantic data specification that prescribes structured and standardized formats for the organization, description, and interpretation of data to ensure attribute conformity, semantic consistency, and interoperable exchange among systems, applications, and users, independent of the media type. 
    :param str schemaMediaType: media type according to IETF RFC 6838,  shall filter for the distribution of the data model schema the attribute conforms to. 
    :return: 
    
    .. code-block:: json
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

    In case of error the value is replaced with an error code

.. py:function:: FindAuthenticSource(queryType, attributeIdentifier, country)
    :noindex:

    This interface is implemented by a Data Service Directory which is a registry of authentic sources and their data services. The Data Service Directory can be globally unique and contain a global registry of all             authentic sources or most likely is regional (e.g. in EU) or national. In this case, the interface FindDataServiceDirectory is useful to find the endpoint of the relevant regional or national Data Service             Directory. 
    This interface allows to search the metadata of the authentic source(s) that support data services (verification, retrieval etc.) for the queried attribute(s). 
    The assumption is that a Data Service Directory supports one semantic repository i.e. all authentic sources registered in the Data Service Directory share the same semantic repository.
    NOTE: why not extending this to search for provider as well?

    **Authorization**: none

    :param str(fixed: `dataServices`) queryType: Query type; must be `dataServices`
    :param str:uri attributeIdentifier: Unique URI identifier for the attribute
    :param str country: Filter data services by country code (ISO 3166-1 alpha-2)
    :return: 
    
    .. code-block:: json

          {
            "dataServices": [
              {
                "attributeIdentifier": "<string:uri>",
                "endpointDescription": "<string:uri>",
                "endpointURI": "<string:uri>",
                "provider": {
                  "legalName": "<string>",
                  "identifiers": [
                    {
                      "type": "<string:uri>",
                      "identifier": "<string>"
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

    In case of error the value is replaced with an error code

.. py:function:: FindDataServiceDirectory(country)
    :noindex:

    This interface allows to search the endpoint of the relevant regional or national Data Service Directory and the semantic repositiry that the Data Service Directory supports. 

    **Authorization**: none

    :param str country: country code of the targeted country (ISO 3166-1 alpha-2)
    :return: 
    
    .. code-block:: json

          {
            "DSDuri": "<string:uri>",
            "SRuri": "<string:uri>",
            "country" : ["<string:iso3166-alpha2>"]
          }
    
    In case of error the value is replaced with an error code

.. py:function:: verifyIdentity(attributes, attributeFragments, attributeSet, mandate)
    :noindex:

    Verify attributes against the authentic source without retrieving full data. Supports full attribute verification, fragment verification (privacy-preserving using JSONPath), or both.
    In the case of attributes or attributesFragment, the verification provides a result for each attribute. 
    In the case of attributeSet, the verification is matching all provided identity attributes in the set and computes a global matching result.
    The required identification data of the user shall be contained in the access token provided by the Authorization Server.

    **Authorization**: `id.verify`

    :param array attributes: Attributes to verify (conditional: required if attributeFragments absent)
    :param array attributeFragments: Attribute fragments for privacy-preserving verification (conditional: required if attributes absent) using the JSONPath language according to IETF RFC 9535
    :param array attributeSet: A set of identity attributes associated to a unique URI and to be verified from the authentic source
    :param object mandate: Mandate for delegated access on behalf of another data subject
    :return: 
    
    .. code-block:: json

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
            "AttributeSetResults": [
              {
                "attributeSetIdentifier": "<string:uri>",
                "location": "<string:jsonpath>",
                "attributeSetVerificationResult": "<string:uri:enum(Match|NoMatch|MatchWithVariation|Unknown)>",
                "VerificationResult": "<string:enum(Match|NoMatch|MatchWithVariation|Unknown)>",
                "fragmentValue": "<any>"
              }
            ],
            "mandateResult": "<MandateResult>"
          }
    
    In case of error the value is replaced with an error code

.. py:function:: readAttributes(attributes, attributeSet, mandate)
    :noindex:

    Retrieve actual attribute values from the authentic source.
    The required identification data of the user shall be contained in the access token provided by the Authorization Server.

    **Authorization**: `id.read`

    :param array attributes: URIs of attributes to retrieved from the authentic source (min 1)
    :param array attributeSet: A set of identity attributes associated to a unique URI and to be retrieved from the authentic source
    :param object mandate: Mandate for delegated retrieval on behalf of another data subject
    :return: 
    
    .. code-block:: json

          {
            "responseId": "<string:uuid>",
            "provider": "<Provider>",
            "authenticSource": "<Provider>",
            "attributeReadResults": [
              {
                "attributeIdentifier": "<string:uri>",
                "attributeValue": "<object>",
                "stringRetrieveResult": "<string:enum(Success|Failure)>"
              }
            ],
            "attributeSetReadResults": [
              {
                "attributeSetIdentifier": "<string:uri>",
          
                "attributes": [
                  {
                    "attributeIdentifier": "<string:uri>",
                    "attributeValue": "<object>",
                    "stringRetrieveResult": "<string:enum(Success|Failure)>"
                  }
                ]
              }
            ],
            "mandateResult": "<MandateResult>"
          }
    
    In case of error the value is replaced with an error code

.. py:function:: identify(attributeSet, outputAttributeSet)
    :noindex:

    Identify possibly matching identities against an input set of attributes. Returns an array of predefined
    datasets as described by outputAttributeSet.

    Note: This service may be limited to some specific government RPs e.g. law enforcement agencies

    **Authorization**: `id.identify`

    :param list[str] attributeSet: A list of pair (name,value) requested
    :param list[str] outputAttributeSet: An array of attributes requested
    :return: json as specified by outputAttributeSet
    
    In case of error (unknown attributes, unauthorized access, etc.) the value is replaced with an error code


Attribute set
"""""""""""""

When identity attributes are exchanged, they are included in an attribute set, possibly containing groups like
biographic data, biometric data, document data, contact data... This structure is extensible and may be complemented
with other data groups, and each group may contain any number of attribute name / attribute value pairs.

Attribute set name
""""""""""""""""""

Attribute sets are by definition structures with variable and optional content, hence it may be useful to pre-agree
on a given attribute set content and name between two or more systems in a given project scope.

Any string may be used to define an attribute set name, but in the scope of this specification following names are
reserved and predefined:

.. list-table::
    :header-rows: 1

    * - Name
      - Description
      - Data Included
    * - "DEFAULT_SET_01"
      - Minimum demographic data
      - - First name
        - Last name
        - DoB
        - Place of birth
    * - "DEFAULT_SET_02"
      - Minimum demographic and portrait
      - Minimum demographic data + portrait
    * - "DEFAULT_SET_EIDAS"
      - Set expected to comply with eIDAS pivotal attributes [#]_.
      - Mandatory attributes:

        - First name
        - Last name
        - DoB
        - Identifier 

        Optional attributes:

        - Birth name 
        - Place of birth 
        - Gender
        - Current address



Output Attribute set
""""""""""""""""""""

To specify what identity attributes are expected in return when performing e.g. an identify request or a read attributes.

Data Model
""""""""""

.. list-table:: Authentic Source Data Model
    :header-rows: 1
    :widths: 25 50 25

    * - Type
      - Description
      - Example

    * - LocalizedText
      - A text value with its associated language code (ISO 639-1).
        Contains ``value`` (string) and ``language`` (string).
      - ``{"value": "Date of Birth", "language": "en"}``

    * - Provider
      - Legal entity operating as ASIP or DIP. Contains ``legalName`` (string),
        ``identifiers`` (array of ProviderIdentifier), ``establishedByLaw`` (EstablishedByLaw),
        and ``currentAddress`` (string).
      - ``{"legalName": "Ministry of Interior", "country": "FR"}``

    * - ProviderIdentifier
      - Typed identifier for a provider. Contains ``type`` (URI identifying the scheme)
        and ``identifier`` (string value within the scheme).
      - ``{"type": "urn:etsi:uri:vatin", "identifier": "FR12345678901"}``

    * - EstablishedByLaw
      - Legal basis for public sector entities. Contains ``legislativeIdentifier`` (URI)
        and ``legalBasis`` (human-readable description).
      - ``{"legalBasis": "Law 2021-123 on digital identity"}``

    * - VerificationAttribute
      - Complete attribute to verify against authentic source. Contains
        ``attributeIdentifier`` (URI) and ``attributeValue`` (JSON object).
      - ``{"attributeIdentifier": "urn:etsi:19478:attribute:naturalperson:DateOfBirth/v1.0", "attributeValue": {"date": "1990-05-15"}}``

    * - AttributeFragment
      - Privacy-preserving fragment for verification using JSONPath. Contains
        ``attributeIdentifier`` (URI), ``location`` (JSONPath expression), and ``value`` (any).
      - ``{"attributeIdentifier": "urn:...:DateOfBirth/v1.0", "location": "$.year", "value": 1990}``

    * - AttributeVerificationResult
      - Result for a verified attribute. Contains ``attributeIdentifier`` (URI),
        ``attributeVerificationResult`` (URI enum: Match, NoMatch, MatchWithVariation, Unknown),
        ``VerificationResult`` (string), and ``attributeValue`` (object, conditional).
      - ``{"attributeVerificationResult": "http://uri.etsi.org/19478/VerificationResult/Match"}``

    * - FragmentVerificationResult
      - Result for a verified fragment. Contains ``attributeIdentifier`` (URI),
        ``location`` (JSONPath), ``fragmentVerificationResult`` (URI enum),
        ``VerificationResult`` (string), and ``fragmentValue`` (any, conditional).
      - ``{"location": "$.year", "fragmentVerificationResult": ".../Match"}``

    * - SchemaDistribution
      - Location where an attribute schema can be accessed. Contains ``accessURL`` (URI)
        and ``mediaType`` (string).
      - ``{"accessURL": "https://example.eu/schemas/dob.json", "mediaType": "application/json"}``

    * - DataService
      - Data service endpoint for verification/retrieval. Contains ``attributeIdentifier`` (URI),
        ``endpointDescription`` (URI to API spec), ``endpointURI`` (base URL),
        ``provider`` (Provider), and ``country`` (ISO 3166-1 alpha-2).
      - ``{"endpointURI": "https://as.example.eu/api/v1"}``

    * - Mandate
      - Delegated authority for acting on behalf of another data subject. Contains
        ``mandateType`` (string), ``mandateReference`` (string), ``delegator`` (object),
        ``delegate`` (object), ``validFrom``, ``validUntil`` (date-time), and ``scope`` (array of URI).
      - ``{"mandateType": "LEGAL_REPRESENTATIVE", "mandateReference": "MND-2024-001"}``

    * - MandateResult
      - Outcome of mandate validation. Contains ``mandateValid`` (boolean),
        ``mandateReference`` (string), ``validationTime`` (date-time), ``delegatorMatch``,
        ``delegateMatch`` (boolean), and ``validationDetails`` (object).
      - ``{"mandateValid": true, "mandateReference": "MND-2024-001"}``




.. [#] `eIDAS SAML Attribute Profile <https://ec.europa.eu/cefdigital/wiki/download/attachments/82773108/eidas_saml_attribute_profile_v1.0_2.pdf?version=1&modificationDate=1497252920317&api=v2>`_

