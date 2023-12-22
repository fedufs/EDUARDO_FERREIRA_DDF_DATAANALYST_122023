# Libraries
import pandas as pd
import json
import os
from openai import OpenAI
from dotenv import load_dotenv

"""
Function to extract features from a given title and description using OpenAI's GPT-3.5-turbo model.

Parameters:
- client: OpenAI API client for making requests.
- title: A string representing the title of the product.
- description: A string representing the description of the product.

Returns:
A dictionary containing extracted features in JSON format, including keys for "category," "material," and "features."
The "category" key is filled with the best-matched category from a predefined list.
The "material" key is filled with the best-matched primary material from a predefined list.
The "features" key is populated with relevant features extracted from the provided title and description.

Note: If a value is not determinable, it is left as null in the JSON format.
"""

def det_features(client: OpenAI, title: str, description: str) -> dict:
    response = client.chat.completions.create(
          model = "gpt-3.5-turbo",
          temperature = 1,
          messages = [
              {
                  "role": "user",
                  "content": r'''
                    My dataset has two text columns: title and description. 
                    I want to determine the features that will be useful for analysis. Example: 
                    
                    Title: FYY Leather Case with Mirror for Samsung Galaxy S8 Plus, Leather Wallet Flip Folio Case with Mirror and Wrist Strap for Samsung Galaxy S8 Plus Black.
                    
                    Description: Premium PU Leather Top quality. Made with Premium PU Leather. Receiver design. 
                    Accurate cut-out for receiver. Convenient to Answer the phone without open the case. 
                    Hand strap makes it easy to carry around. RFID Technique: Radio Frequency Identification technology, through radio signals to identify specific targets and to read and copy electronic data. 
                    Most Credit Cards, Debit Cards, ID Cards are set-in the RFID chip, the RFID reader can easily read the cards information within 10 feet(about 3m) without touching them. 
                    This case is designed to protect your cards information from stealing with blocking material of RFID shielding technology. 100% Handmade. 
                    Perfect craftsmanship and reinforced stitching make it even more durable. Sleek, practical, and elegant with a variety of dashing colors. 
                    Multiple Functions Card slots are designed for you to put your photo, debit card, credit card, or ID card while on the go. Unique design. 
                    Cosmetic Mirror inside made for your makeup and beauty. Perfect Viewing Angle. Kickstand function is convenient for movie-watching or video-chatting. 
                    Space amplification, convenient to unlock. Kickstand function is convenient for movie-watching or video-chatting.
                    
                    Features:{
                        "category": "Phone Accessories",
                        "material": "Premium PU Leather",
                        "features": {
                          "receiver_design": "Accurate cut-out for receiver. Convenient to Answer the phone without opening the case.",
                          "hand_strap": "Yes",
                          "RFID_technique": "Protection of card information with RFID shielding technology",
                          "handmade": "100% Handmade",
                          "stitching": "Reinforced stitching",
                          "functions": {
                            "card_slots": "Yes",
                            "cosmetic_mirror": "Yes",
                            "kickstand_function": "Yes, convenient for movie-watching or video-chatting",
                            "space_amplification": "Yes, convenient to unlock"
                          },
                          "color_options": "Variety of dashing colors",
                          "compatibility": "Samsung Galaxy S8 Plus"
                        }
                    }
                  '''
              },
              {
                  "role": "user",
                  "content": rf'''
                    So, what will be the features of a column with the title {title} and description {description}?
                    
                    Answer me using a JSON format, using just the keys: category, material, features. 

                    Please, pay attention to the example above and at the orders below.

                    On the category key, fill it with just one and the best general category found in the corresponding text or title: Electronics, Clothing, Home and Kitchen, Beauty and Personal Care, Books, Toys and Games, Sports and Outdoors Equipment, Furniture, Health and Wellness, Automotive Accessories, Pet Supplies, Jewelry, Office Supplies, Home Decor, Baby and Toddler, Tools, Grocery and Gourmet Food, Fitness and Exercise, Outdoor Clothing and Gear, Musical Instruments, Arts and Crafts Supplies, Party Supplies, Travel Accessories, Computer Accessories, Mobile Phones and Accessories, Cameras and Photography Equipment, Bedding and Linens, Shoes, Watches, Sunglasses, Handbags and Wallets, School and Educational Supplies, Video Games and Consoles, Collectibles, DIY and Home Improvement Tools, Food and Beverage, Camping Gear, Hobbies and Collectibles, Home Cleaning Products, Stationery, Home Security Systems, Gardening Supplies, Board Games, Cookware and Bakeware, Fishing Gear, Educational Toys, Luggage and Travel Bags, Home Entertainment Systems, Smart Home Devices.

                    Please, do not leave the category key null. Fill it with just one and the best corresponding category at the list above or find it on the internet.

                    On the material key, extract with just one and the best primary material that fits with the corresponding title or text: Cotton, Plastic, Metal, Leather, Wood, Glass, Paper, Polyester, Nylon, Rubber, Ceramic, Paper, Cardboard, Silicone, Stainless steel, Aluminum, Bamboo, Velour, Wool, Linen, Velvet, Mesh, Polyethylene, Acrylic, Latex, Canvas, Denim, Satin, Silk, Spandex, Microfiber, Polypropylene, Polyurethane, Felt, Fleece, Brass, Copper, Granite, Marble, PVC, Laminate, Melamine, Acetate, Tulle, Jute, Neoprene, Vinyl, Lycra, Suede.

                    Please, do not leave the material key null. Fill it with just one and the best corresponding primary material at the list above or find it on the internet.

                    Separate the features in a smart way as shown at the example.
                    Please, answer me with just a JSON format and don't use any other text.
                    And if you don't know some value, just leave it null.
                                        
                    Show me your best, I trust you.
                    '''
              }
          ]
      )
    return json.loads(response.choices[0].message.content)


if __name__ == '__main__':
    # Load environment variables
    load_dotenv()

    # Configure the OpenAI client
    client = OpenAI(api_key = os.getenv("OPEN_AI_API_KEY"), organization = os.getenv("OPEN_AI_ORGANIZATION_KEY"))

    # Load the DataFrame
    product_sc = pd.read_csv(r"tb__3mochw__stream_product_search_corpus_eduardo_ferreira_2023-12-19T20_41_51.910683Z.csv")

    # Iterate over the DataFrame and add the features
    for index, row in product_sc.iterrows():
        for key, value in det_features(client = client, title = row['Title'], description = row['Text']).items():
            if key not in product_sc.columns:
                product_sc[key] = None
            product_sc.at[index, key] = str(value)

    # Save the resulting DataFrame as a CSV file
    product_sc.to_csv("result.csv", index = False)