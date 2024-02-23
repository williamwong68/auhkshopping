'''
CREATING A NEW DATABASE
-----------------------
Read explanation here: https://flask-sqlalchemy.palletsprojects.com/en/2.x/contexts/

In the terminal navigate to the project folder just above the miltontours package
Type 'python' to enter the python interpreter. You should see '>>>'
In python interpreter type the following (hitting enter after each line):
    from auhkshopping import db, create_app
    db.create_all(app=create_app())
The database should be created. Exit python interpreter by typing:
    quit()
Use DB Browser for SQLite to check that the structure is as expected before 
continuing.

ENTERING DATA INTO THE EMPTY DATABASE
-------------------------------------

# Option 1: Use DB Browser for SQLite
You can enter data directly into the cities or tours table by selecting it in
Browse Data and clicking the New Record button. The id field will be created
automatically. However be careful as you will get errors if you do not abide by
the expected field type and length. In particular the DateTime field must be of
the format: 2020-05-17 00:00:00.000000

# Option 2: Create a database seed function in an Admin Blueprint
See below. This blueprint needs to be enabled in __init__.py and then can be 
accessed via http://127.0.0.1:5000/admin/dbseed/
Database constraints mean that it can only be used on a fresh empty database
otherwise it will error. This blueprint should be removed (or commented out)
from the __init__.py after use.

Use DB Browser for SQLite to check that the data is as expected before 
continuing.
'''

from flask import Blueprint
from . import db
from .models import Brand, Product, Order
import datetime

bp = Blueprint('admin', __name__, url_prefix='/admin/')

# function to put some seed data in the database
@bp.route('/dbseed/')
def dbseed():
    brand1 = Brand (name = 'Kiehls', image = 'kiehls.jpeg',\
        description = '''Kiehls is the brand that very care of their customer's skin, so all of their product are using natural ingredients to manufacture their products.
        They have several type of products, for example for hair, for body, and skincare. Kiehl's even seperate for men and women products.''')
    brand2 = Brand (name = 'Twinings', image = 'twinings.jpeg',\
        description = '''For Twinings, they like to talk about tea. That's because for them, it's the most exciting thing in the world. With a host of Master Blenders and flavour exprts,
        they pride themselves on challenging the status quo of tea. With a history dating back to 1706, quliaty tea has always been at the heart of what they do.
        Renowned for crfeating vibrant and aromatic blends that are loved by all, from Earl Grey and English Breaskfast to Chai and super fruity infusions, they know the details that matter most.''')
    brand3 = Brand (name = 'Life Space', image = 'lifespace.jpeg',\
        description = '''Life Space care about your health and their products are support healthy immune system function, digestive health and general wellbeing for your family. And their products are take care from
        babies to elders health. They also produce product for pregnant and breastfeeding women to provide the healthy life for their babies.''')
    brand4 = Brand (name = 'Blackmores', image = 'blackmores.jpeg',\
        description = '''lackmores is Australia’s leading natural health company. Based on the vision of our founder Maurice Blackmore (1906-1977), we are passionate about natural health and inspiring people to take 
        control of and invest in their wellbeing. We develop high quality products and services that deliver a more natural approach to health, based on our expertise in vitamins, minerals, herbs and nutrients.''')

    try:
        db.session.add(brand1)
        db.session.add(brand2)
        db.session.add(brand3)
        db.session.add(brand4)
        db.session.commit()
    except:
        return 'There was an issue adding the brands in dbseed function'

    p1 = Product (brand_id = brand1.id, image = 'p_toner.jpg', price = 400,\
        date = datetime.datetime(2021, 3, 12),\
        name = 'Calendula Herbal Extract Alcohol-Free Toner 500ml',\
        description = 'This facial toner is formulated with a blend of Calendula, Great Burdock Root and Allantoin, which are known for their skin soothing properties. The Calendula petals are carefully hand-picked, and inserted into the formula by hand, and work to improve the look and feel of skin.')
    p2 = Product (brand_id = brand1.id, image = 'p_creameye.jpg', price = 365,\
        date = datetime.datetime(2021, 3, 18),\
        name = 'Creamy Eye Treatment with Avocado 28ml',\
        description = 'Re-boot tired eyes with creamy hydration. This nourishing under eye cream is formulated with avocado oil and suitable for all skin types. The unique water-in-oil architecture bursts with lasting hydration while simultaneously forming a physical shield for the under-eye to provide essential care and protection to the delicate under-eye area. The formula gently moisturises the eye area without migrating into the eyes. Can be used under eye makeup as it contains highly effective natural ingredients that provide essential hydration and protection. After uses the eye area is left softer, suppler, and youthful-looking.')
    p3 = Product (brand_id = brand1.id, image = 'p_ultrafacialcream.jpg', price = 380,\
        date = datetime.datetime(2021, 4, 2),\
        name = 'Ultra Facial Cream 125ml',\
        description = 'The Kiehl’s number one moisturising cream is a hydrating face cream which is lightweight, non-greasy and provides 24-hour hydration. Our Ultra Facial Cream instantly leaves skin 2.3x more hydrated, even in skin’s driest areas.The unique formula is thick and creamy as well as being light and absorbs easily into skin. Ultra Facial Cream contains squalane which replenishes fatty acids and antioxidants in the skin’s natural barrier and Glacial Glycoprotein Extract which helps shield the skin from environmental damage and the cold. This gentle formula also includes avocado oil, apricot kernel oil, rice bran oil, olive fruit oil, vitamin e, as well as salicylic acid to remove dryness and leave your skin feeling smooth and soft. Created for all skin types and suitable for sensitive skin, the ultra facial cream is a daily moisturiser that prepares, plumps and protects your skin for the day.')
    p4 = Product (brand_id = brand1.id, image = 'p_clearlycorrect.jpg', price = 700,\
        date = datetime.datetime(2021, 4, 8),\
        name = 'Clearly Corrective™ Dark Spot Solution 100ml',\
        description = 'A targeted dark spot corrector that helps boost radiance and improve skin clarity. Formulated with Activated C plus White Birch and Peony Extracts, this efficacious facial serum for dark spots helps visibly brighten skin and diminish the number and intensity of dark spots and skin discolorations over time.')
    p5 = Product (brand_id = brand2.id, image = 'p_englishbreakfast.png', price = 80,\
        date = datetime.datetime(2021, 4, 12),\
        name = 'Twinings English Breakfast 100packs',\
        description = 'Rejuvenate yourself and welcome in the day. Getting up in the morning with our English Breakfast is a little easier. This full-bodied blend is rich and invigorating and will give you a warm, lovely wake-up, allowing you to embrace the day. As the name suggests, it is perfect for breakfast but also beautiful to enjoy in the afternoon.')
    p6 = Product (brand_id = brand2.id, image = 'p_extrastrongenglish.jpg', price = 80,\
        date = datetime.datetime(2021, 4, 12),\
        name = 'Twinings English Breakfast Extra Strong 80packs',\
        description = 'Your favourite tea intensified… Our Extra Strong English Breakfast tea delivers the full bodied flavour you love, with an added intensity to invigorate you when you need it the most. Enjoy the richness of flavour, and allow this blend to awaken your senses, and tantalise your tastebuds. This tea will become your morning ritual, the perfect way to start your day.')
    p7 = Product (brand_id = brand2.id, image = 'p_earlgrey.png', price = 80,\
        date = datetime.datetime(2021, 4, 12),\
        name = 'Twinings Earl Grey 100packs',\
        description = 'A tea fit for an Earl! Legend has it that Earl Grey was developed especially for the 2nd Earl of England in the 1800s. It is light and aromatic with a distinctive citrus bergamot flavour. So sip and enjoy this delightful blend inspired by the Earl and you will feel like you have just stepped back in time.')
    p8 = Product (brand_id = brand2.id, image = 'p_ausafternoon.png', price = 80,\
        date = datetime.datetime(2021, 4, 12),\
        name = 'Twinings Australian Afternoon',\
        description = 'The perfect blend for Australia. Excite your taste buds with our Australian Afternoon blend. This brisk, full-bodied blend was created with Australians for Australians. It\'s the perfect pick-me-up and is sure to liven up your day. We think you\'ll agree it’s as vibrant and wonderful as this beautiful country!')
    p9 = Product (brand_id = brand2.id, image = 'p_irish.png', price = 80,\
        date = datetime.datetime(2021, 4, 12),\
        name = 'Twinings Irish Breakfast 100packs',\
        description = 'Tea to inspire a hearty laugh. Like the beautiful country that this tea is named after, Irish Breakfast is comforting and lively at the same time. This wonderfuly brisk blend will have you sharing stories with friends over a pot to be sure, to be sure! Enjoy with breakfast or anytime you have a funny tale to tell.')
    p10 = Product (brand_id = brand2.id, image = 'p_lady.png', price = 80,\
        date = datetime.datetime(2021, 4, 12),\
        name = 'Twinings Lady Grey 100packs',\
        description = 'To liven your spirit. Just as delicate as our Earl Grey blend, Lady Grey has an added hint of lemon and orange peel. Bright and fragrant, a cup of this tea will be like those perfect long summer afternoons when you were young and free. Enjoy a pot with a friend and reminisce about your childhood!')
    p11 = Product (brand_id = brand3.id, image = 'p_broad.jpg', price = 300,\
        date = datetime.datetime(2021, 4, 20),\
        name = 'Life Space Broad Spectrum Probiotic 60capsules',\
        description = 'Broad Spectrum Probiotic is a premium, multi-strain probiotic containing 15 strains of beneficial bacteria. Specifically formulated to support general health and wellbeing, digestive health and immune health.')
    p12 = Product (brand_id = brand3.id, image = 'p_infant.jpg', price = 300,\
        date = datetime.datetime(2021, 4, 20),\
        name = 'Life Space Probiotic Powder for Infant 60g',\
        description = 'Life-Space Probiotic Powder for Infant is a premium quality, multi-strain probiotic formula containing 8 strains of beneficial bacteria including 2 types that are naturally found in breastmilk. Specifically formulated for infants aged between 1 and 6 months, Probiotic Powder for Infant also contains prebiotic Galacto-oligosaccharide (GOS) along with milk protein Lactoferrin.')
    p13 = Product (brand_id = brand3.id, image = 'p_probiotic.jpg', price = 300,\
        date = datetime.datetime(2021, 4, 20),\
        name = 'Life Space Probiotic for 60+ Years',\
        description = 'Australia\'s No.1 Senior Probiotics.* A premium probiotic formula containing 15 strains of beneficial bacteria, to support general wellbeing and help enhance immune system function in the elderly. Contains 5 strains of Bifidobacteria which may decline naturally in people over the age of 60 years.')
    p14 = Product (brand_id = brand3.id, image = 'p_women.jpg', price = 300,\
        date = datetime.datetime(2021, 4, 20),\
        name = 'Life Space Urogen™ Probiotic for Women 60capsules',\
        description = 'Australia\'s No.1 Women\'s Probiotic.* A premium probiotic containing 5 strains of beneficial bacteria in combination with cranberry.')
    p15 = Product (brand_id = brand4.id, image = 'p_multivita.jpg', price = 350,\
        date = datetime.datetime(2021, 4, 28),\
        name = 'Blackmores Multivitamin for Men 150 capsules',\
        description = 'A comprehensive blend of vitamins & minerals, designed to support men’s health and wellbeing.')
    p16 = Product (brand_id = brand4.id, image = 'p_nails.jpg', price = 100,\
        date = datetime.datetime(2021, 4, 28),\
        name = 'Blackmores Hair, Skin & Nail 60capsules',\
        description = 'Blackmores Nails, Hair & Skin is a comprehensive formula that provides essential nutrients for healthy nails, hair and skin. It supports collagen formation and reduces nail brittleness & splitting.')
    p17 = Product (brand_id = brand4.id, image = 'p_coq.jpg', price = 160,\
        date = datetime.datetime(2021, 5, 3),\
        name = 'Blackmores CoQ10 150mg 90capsules',\
        description = 'Blackmores CoQ10 150mg is a source of coenzyme Q10 (CoQ10), an antioxidant enzyme that is found naturally concentrated in the heart muscle. CoQ10 150mg maintains heart health and helps in the maintenance of healthy blood lipids. CoQ10 levels naturally decline with age and supplementation helps maintain and support CoQ10 levels in the body. CoQ10 is an antioxidant and reduces free radical formed in the body.')
    p18 = Product (brand_id = brand4.id, image = 'p_joint.jpg', price = 240,\
        date = datetime.datetime(2021, 5, 5),\
        name = 'Blackmores Joint Formula Advanced 120Tablets',\
        description = 'Blackmores Joint Formula Advanced has been specifically formulated to contain glucosamine, chondroitin, manganese and boron which reduces symptoms of osteoarthritis including mild joint inflammation swelling aches and pain, reduce joint stiffness, maintain healthy joint cartilage production in a vanilla flavoured, two a day tablet.')
    
    try:
        db.session.add(p1)
        db.session.add(p2)
        db.session.add(p3)
        db.session.add(p4)
        db.session.add(p5)
        db.session.add(p6)
        db.session.add(p7)
        db.session.add(p8)
        db.session.add(p9)
        db.session.add(p10)
        db.session.add(p11)
        db.session.add(p12)
        db.session.add(p13)
        db.session.add(p14)
        db.session.add(p15)
        db.session.add(p16)
        db.session.add(p17)
        db.session.add(p18)
        db.session.commit()
    except:
        return 'There was an issue adding a product in dbseed function'
    
    return 'DATA LOADED'