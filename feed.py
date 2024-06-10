import yaml
import xml.etree.ElementTree as xml_tree

with open("feed.yaml", "r") as file:
    yaml_data = yaml.safe_load(file)

    rss_element = xml_tree.Element(
        "rss",
        {
            "version": "2.0",
            "xmlns:itunes": "http://www.itunes.com/dtds/podcast-1.0.dtd",
            "xmlns:content": "http://purl.org/rss/1.0/modules/content/",
            "xml:lang": "en-US",
        },
    )

    channel_element = xml_tree.SubElement(rss_element, "channel")
    link_prefix = yaml_data["link"]

    owner_element = xml_tree.SubElement(channel_element, "itunes:owner")
    xml_tree.SubElement(owner_element, "itunes:name").text = yaml_data["author"]
    xml_tree.SubElement(owner_element, "itunes:email").text = "info@raybo.org"
    xml_tree.SubElement(channel_element, "title").text = yaml_data["title"]
    xml_tree.SubElement(channel_element, "link").text = link_prefix + "/podcast.xml"
    xml_tree.SubElement(channel_element, "language").text = yaml_data["language"]
    xml_tree.SubElement(channel_element, "itunes:author").text = yaml_data["author"]
    xml_tree.SubElement(channel_element, "description").text = yaml_data["description"]
    xml_tree.SubElement(
        channel_element, "itunes:image", {"href": link_prefix + yaml_data["image"]}
    )
    xml_tree.SubElement(
        channel_element, "itunes:category", {"text": yaml_data["category"]}
    )
    # xml_tree.SubElement(channel_element, 'format').text = yaml_data['format']
    # xml_tree.SubElement(channel_element, 'subtitle').text = yaml_data['subtitle']
    xml_tree.SubElement(
        channel_element,
        "atom:link",
        {
            "xmlns:atom": "http://www.w3.org/2005/Atom",
            "rel": "self",
            "type": "application/rss+xml",
            "href": link_prefix + "/podcast.xml",
        },
    )

    for item in yaml_data["item"]:
        item_element = xml_tree.SubElement(channel_element, "item")
        xml_tree.SubElement(item_element, "itunes:title").text = item["title"]
        # '<![CDATA['+item['description']+']]>' <get's encoded to &lt;
        xml_tree.SubElement(item_element, "description").text = item["description"]
        enclosure = xml_tree.SubElement(
            item_element,
            "enclosure",
            {
                "length": item["length"].replace(",", ""),
                "type": "audio/mpeg",
                "url": link_prefix + item["file"],
            },
        )
        xml_tree.SubElement(item_element, "guid").text = link_prefix + item["file"]
        xml_tree.SubElement(item_element, "itunes:author").text = yaml_data["author"]
        xml_tree.SubElement(item_element, "pubDate").text = item["published"]
        xml_tree.SubElement(item_element, "itunes:duration").text = item["duration"]
        xml_tree.SubElement(item_element, "itunes:explicit").text = "false"

    output_tree = xml_tree.ElementTree(rss_element)
    output_tree.write("podcast.xml", encoding="UTF-8", xml_declaration=True)
