# corpus-search-static-sources

* This repo exposes basic metadata about projects/texts in OAI-PMH ListRecords format (see below).
* Data exposed through this repo need to be registered in [dse-static-oai-pmh's config](https://github.com/acdh-oeaw/dse-static-oai-pmh/blob/main/app/config.py)

```xml
<OAI-PMH xmlns="http://www.openarchives.org/OAI/2.0/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.openarchives.org/OAI/2.0/          http://www.openarchives.org/OAI/2.0/OAI-PMH.xsd">
    <responseDate>2026-03-12T05:54:49Z</responseDate>
    <request verb="ListRecords" metadataPrefix="oai_dc">
        https://schnitzler-briefe.acdh.oeaw.ac.at/oai-pmh
    </request>
    <ListRecords>
        <record>
            <header>
                <identifier>L00001.xml</identifier>
                <datestamp>2026-03-12</datestamp>
            </header>
            <metadata>
                <oai_dc:dc xmlns:oai_dc="http://www.openarchives.org/OAI/2.0/oai_dc/" xmlns:dc="http://purl.org/dc/elements/1.1/" xsi:schemaLocation="http://www.openarchives.org/OAI/2.0/oai_dc/                             http://www.openarchives.org/OAI/2.0/oai_dc.xsd">
                    <dc:title>Fedor Mamroth an Arthur Schnitzler, 2. 8. 1889</dc:title>
                    <dc:type>Text</dc:type>
                    <dc:identifier>https://arthur-schnitzler.github.io/schnitzler-briefe-static/L00001.xml</dc:identifier>
                    <dc:language>deu</dc:language></oai_dc:dc>
            </metadata>
        </record>
    </ListRecords>
</OAI-PMH>
```
        