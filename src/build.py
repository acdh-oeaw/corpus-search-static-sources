import json
import os

html_start = """<!doctype html>
<html lang="en">

<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>corpus-search-static-sources</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css" rel="stylesheet"
    integrity="sha384-sRIl4kxILFvY47J16cr9ZwB07vP4J8+LH7qKQnuqkuIAvNWLzeN8tE5YBujZqJLB" crossorigin="anonymous">
</head>

  <body>
    <div class="container">
      <h1>corpus-search-static-sources</h1>
      <ul>
        <li>This repo exposes basic metadata about projects/texts in OAI-PMH ListRecords format (see below).</li>
        <li>Data exposed through this repo need to be registered in <a
            href="https://github.com/acdh-oeaw/dse-static-oai-pmh/blob/main/app/config.py">dse-static-oai-pmh's config</a>
        </li>
      </ul>
      <h2>endpoints</h2>
      <ul>"""
html_end = """
      </ul>

      <h2>link to code repo</h2>
      <div>
        <a
          href="https://github.com/acdh-oeaw/corpus-search-static-sources">https://github.com/acdh-oeaw/corpus-search-static-sources</a>
      </div>
    </div>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/js/bootstrap.bundle.min.js"
      integrity="sha384-FKyoEForCGlyvwx9Hj09JcYn3nv7wiPVlz7YYwJrWVcXK/BmnVDxM+D2scQbITxI"
      crossorigin="anonymous"></script>
  </body>

</html>
"""
data_file = os.path.join("src", "config.json")
output_file = os.path.join("html", "index.html")

with open(data_file, "r", encoding="utf-8") as fp:
    data = json.load(fp)

items = []
for key, value in data.items():
  identify_out = os.path.join("html", key, "oai-pmh", "Identify.xml")
  print(identify_out)
  identify = f"""
<OAI-PMH xsi:schemaLocation="http://www.openarchives.org/OAI/2.0/ http://www.openarchives.org/OAI/2.0/OAI-PMH.xsd">
  <responseDate>2026-03-16T10:26:17Z</responseDate>
  <request verb="Identify">{value["base_url"]}</request>
  <Identify>
    <repositoryName>{value["title"]}</repositoryName>
    <baseURL>{value["base_url"]}</baseURL>
    <protocolVersion>2.0</protocolVersion>
    <adminEmail>acdh-tech@oeaw.ac.at</adminEmail>
    <earliestDatestamp>2025-04-01T05:24:43Z</earliestDatestamp>
    <deletedRecord>no</deletedRecord>
    <granularity>YYYY-MM-DDThh:mm:ssZ</granularity>
  </Identify>
</OAI-PMH>
"""
  with open(identify_out, "w", encoding="utf-8") as fp:
    fp.write(identify)
  item = f"""
      <li>
        <a href="{key}/oai-pmh/ListRecords.xml">{value["title"]}</a>
      </li>"""
  items.append(item)


result = html_start + "".join(items) + html_end
with open(output_file, "w", encoding="utf-8") as fp:
    fp.write(result)