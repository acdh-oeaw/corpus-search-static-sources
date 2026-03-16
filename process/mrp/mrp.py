import pandas as pd
import os
from datetime import date

today = date.today().isoformat()

df = pd.read_csv("process/mrp/mrp.csv")
df["year"] = df["Titel"].str.extract(r"(\d{4})")

out_dir = os.path.join("html", "mrp", "oai-pmh")
out_file = os.path.join(out_dir, "ListRecords.xml")

os.makedirs(out_dir, exist_ok=True)

filtered_df = df[df["Dokument"].str.contains("-P-0", regex=False, na=False)]

url = "https://mrp.oeaw.ac.at/resolver/resolve-doc.xql?doc-name={}&collection=editions"

records = []

oai_start = """
<OAI-PMH xmlns="http://www.openarchives.org/OAI/2.0/"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xsi:schemaLocation="http://www.openarchives.org/OAI/2.0/ http://www.openarchives.org/OAI/2.0/OAI-PMH.xsd">
    <responseDate>2025-12-22T15:18:01Z</responseDate>
    <request verb="ListRecords" metadataPrefix="oai_dc">
        https://acdh-oeaw.github.io/corpus-search-static-sources
    </request>
    <ListRecords>
"""

oai_end = """
    </ListRecords>
</OAI-PMH>
"""


for i, row in filtered_df.iterrows():
    doc_id = row["Dokument"]
    url = f"https://mrp.oeaw.ac.at/resolver/resolve-doc.xql?doc-name={doc_id}"
    record_stub = f"""
<record>
    <header>
        <identifier>{doc_id}</identifier>
        <datestamp>{today}</datestamp>
    </header>
    <metadata>
        <oai_dc:dc xmlns:oai_dc="http://www.openarchives.org/OAI/2.0/oai_dc/"
            xmlns:dc="http://purl.org/dc/elements/1.1/"
            xsi:schemaLocation="http://www.openarchives.org/OAI/2.0/oai_dc/ http://www.openarchives.org/OAI/2.0/oai_dc.xsd">
            <dc:title>{row["Titel"]}</dc:title>
            <dc:type>Text</dc:type>
            <dc:date>{row["year"]}</dc:date>
            <dc:identifier>{url}</dc:identifier>
            <dc:language>deu</dc:language>
        </oai_dc:dc>
    </metadata>
</record>
"""
    records.append(record_stub)
output = oai_start + "".join(records) + oai_end
with open(out_file, "w", encoding="utf-8") as fp:
    fp.write(output)
