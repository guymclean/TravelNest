from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import json


def createJsonObj(url):
	req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
	html = urlopen(req).read()
	soup = BeautifulSoup(html, "html.parser")
	jsonStr = soup.find("script", attrs={'data-hypernova-key': "spaspabundlejs"}).get_text()[4:-3]
	jsonObj = json.loads(jsonStr)["bootstrapData"]["reduxData"]["homePDP"]["listingInfo"]["listing"]
	return jsonObj


def createPropertyObj(jsonObj):
	propertyName = jsonObj["name"]
	propertyType = jsonObj["room_and_property_type"]
	numOfBeds = jsonObj["bed_label"].split(" ")[0]
	numOfBaths = jsonObj["bathroom_label"].split(" ")[0]
	amenities = []
	for amenity in jsonObj["listing_amenities"]:
		amenities.append(amenity["name"])

	propertyObj = {
		"name": propertyName,
		"type": propertyType,
		"beds": numOfBeds,
		"baths": numOfBaths,
		"amenities": amenities
	}
	return propertyObj


def printPropertyDetails(propertyObj):
	print("Property name: ", propertyObj["name"])
	print("Property type: ", propertyObj["type"])
	print("Beds: ", propertyObj["beds"])
	print("Bathrooms: ", propertyObj["baths"])
	print("Amenities: ")
	for amenity in propertyObj["amenities"]:
		print(" - ", amenity)
	print("")


def main():
	urls = ["https://www.airbnb.co.uk/rooms/14531512?s=51",
			"https://www.airbnb.co.uk/rooms/19278160?s=51",
			"https://www.airbnb.co.uk/rooms/19292873?s=51"]
	for url in urls:
		jsonObj = createJsonObj(url)
		propertyObj = createPropertyObj(jsonObj)
		printPropertyDetails(propertyObj)


main()
