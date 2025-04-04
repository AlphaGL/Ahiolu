from django.db import models
# from django.contrib.auth.models import User  # For customer ratings
from django.conf import settings # Custom User Authentication

# ===========================
#  CATEGORY MODEL (LOCATIONS)
# ===========================

class LocationCategory(models.Model):
    CATEGORY_CHOICES = [
        ('all', 'All Categories'),
        ('tech', 'Technology'),
        ('science', 'Science'),
        ('arts', 'Arts'),
        ('business', 'Business'),
        ('finance', 'Finance'),
        ('health', 'Health & Wellness'),
        ('education', 'Education'),
        ('sports', 'Sports'),
        ('gaming', 'Gaming'),
        ('entertainment', 'Entertainment'),
        ('travel', 'Travel & Tourism'),
        ('food', 'Food & Cooking'),
        ('fashion', 'Fashion & Beauty'),
        ('automobile', 'Automobiles'),
        ('real_estate', 'Real Estate'),
        ('music', 'Music'),
        ('movies', 'Movies & TV Shows'),
        ('cryptocurrency', 'Cryptocurrency'),
        ('environment', 'Environment & Sustainability'),
        ('ai', 'Artificial Intelligence'),
        ('literature', 'Literature'),
        ('history', 'History'),
        ('law', 'Law & Legal'),
        ('philosophy', 'Philosophy'),
        ('psychology', 'Psychology'),
        ('architecture', 'Architecture'),
        ('engineering', 'Engineering'),
        ('mathematics', 'Mathematics'),
        ('space', 'Space Exploration'),
        ('biology', 'Biology'),
        ('chemistry', 'Chemistry'),
        ('physics', 'Physics'),
        ('geography', 'Geography'),
        ('sociology', 'Sociology'),
        ('politics', 'Politics & Government'),
        ('religion', 'Religion & Spirituality'),
        ('parenting', 'Parenting'),
        ('lifestyle', 'Lifestyle'),
        ('productivity', 'Productivity & Self-Improvement'),
        ('social_media', 'Social Media & Marketing'),
        ('entrepreneurship', 'Entrepreneurship'),
        ('leadership', 'Leadership & Management'),
        ('investing', 'Investing & Stock Market'),
        ('startups', 'Startups'),
        ('design', 'Design & UX/UI'),
        ('photography', 'Photography'),
        ('videography', 'Videography'),
        ('graphic_design', 'Graphic Design'),
        ('podcasting', 'Podcasting'),
        ('writing', 'Writing & Copywriting'),
        ('journalism', 'Journalism'),
        ('news', 'News & Media'),
        ('humor', 'Humor & Satire'),
        ('crafts', 'Crafts & DIY'),
        ('pets', 'Pets & Animals'),
        ('gardening', 'Gardening'),
        ('automotive', 'Automotive Repair & Maintenance'),
        ('furniture', 'Furniture & Home Decor'),
        ('gaming_hardware', 'Gaming Hardware & Equipment'),
        ('personal_finance', 'Personal Finance'),
        ('real_estate_investment', 'Real Estate Investment'),
        ('investing_education', 'Investing Education'),
        ('freelancing', 'Freelancing & Remote Work'),
        ('vlogging', 'Vlogging & YouTube'),
        ('self_defense', 'Self Defense & Safety'),
        ('language_learning', 'Language Learning'),
        ('nutrition', 'Nutrition & Diet'),
        ('beauty', 'Beauty & Cosmetics'),
        ('skincare', 'Skincare & Haircare'),
        ('luxury', 'Luxury & Lifestyle'),
        ('vintage', 'Vintage & Collectibles'),
        ('antiques', 'Antiques'),
        ('gaming_tournaments', 'Gaming Tournaments'),
        ('e_sports', 'E-Sports'),
        ('mobile_technology', 'Mobile Technology'),
        ('blockchain', 'Blockchain Technology'),
        ('cloud_computing', 'Cloud Computing'),
        ('robotics', 'Robotics'),
        ('internet_of_things', 'Internet of Things (IoT)'),
        ('cybersecurity', 'Cybersecurity'),
        ('virtual_reality', 'Virtual Reality (VR)'),
        ('augmented_reality', 'Augmented Reality (AR)'),
        ('wearable_technology', 'Wearable Technology'),
        ('3d_printing', '3D Printing'),
        ('fintech', 'Financial Technology (Fintech)'),
        ('green_technology', 'Green Technology'),
        ('biotechnology', 'Biotechnology'),
        ('genetics', 'Genetics & Genomics'),
        ('pharmacology', 'Pharmacology & Drugs'),
        ('food_science', 'Food Science & Research'),
        ('astronomy', 'Astronomy & Astrophysics'),
        ('marine_science', 'Marine Science & Oceanography'),
        ('geology', 'Geology'),
        ('volunteering', 'Volunteering & Charity Work'),
        ('activism', 'Activism & Social Movements'),
        ('human_rights', 'Human Rights'),
        ('mental_health', 'Mental Health'),
        ('addiction_recovery', 'Addiction Recovery'),
        ('elderly_care', 'Elderly Care & Support'),
        ('women_issues', 'Women\'s Issues'),
        ('disability', 'Disability Rights & Support'),
        ('minimalism', 'Minimalism & Decluttering'),
        ('home_improvement', 'Home Improvement'),
        ('fishing', 'Fishing & Aquatic Sports'),
        ('hiking', 'Hiking & Outdoor Activities'),
        ('camping', 'Camping & Survival Skills'),
        ('cycling', 'Cycling & Mountain Biking'),
        ('yoga', 'Yoga & Meditation'),
        ('pilates', 'Pilates & Physical Fitness'),
        ('dance', 'Dance & Performance Arts'),
        ('sports_gear', 'Sports Gear & Equipment'),
        ('swimming', 'Swimming & Water Sports'),
        ('winter_sports', 'Winter Sports'),
        ('snowboarding', 'Snowboarding & Skiing'),
        ('music_production', 'Music Production & Sound Engineering'),
        ('musical_instruments', 'Musical Instruments & Gear'),
        ('audio_engineering', 'Audio Engineering'),
        ('classical_music', 'Classical Music'),
        ('jazz', 'Jazz Music'),
        ('rock', 'Rock Music'),
        ('pop', 'Pop Music'),
        ('hiphop', 'Hip-Hop Music'),
        ('electronic_music', 'Electronic Music'),
        ('country_music', 'Country Music'),
        ('indie_music', 'Indie Music'),
        ('world_music', 'World Music'),
        ('comedy', 'Comedy & Stand-Up'),
        ('short_films', 'Short Films & Documentaries'),
        ('theater', 'Theater & Performing Arts'),
        ('musicals', 'Musicals & Broadway'),
        ('independent_film', 'Independent Film'),
        ('documentary', 'Documentary Film'),
        ('literature_reviews', 'Literature Reviews'),
        ('book_clubs', 'Book Clubs & Reviews'),
        ('writing_prompts', 'Writing Prompts'),
        ('book_illustrations', 'Book Illustrations & Artwork'),
        ('author_interviews', 'Author Interviews'),
        ('language_arts', 'Language Arts'),
        ('comic_books', 'Comic Books & Graphic Novels'),
        ('manga', 'Manga & Anime'),
        ('fan_fiction', 'Fan Fiction'),
        ('cosplay', 'Cosplay & Costumes'),
        ('conventions', 'Conventions & Expos'),
        ('collectibles', 'Collectibles & Memorabilia'),
        ('esoteric', 'Esoteric & Mysticism'),
        ('astrology', 'Astrology & Horoscopes'),
        ('tarot', 'Tarot & Divination'),
        ('mindfulness', 'Mindfulness & Meditation'),
        ('spirituality', 'Spirituality & Faith'),
        ('personal_growth', 'Personal Growth & Self-Development'),
        ('hobbies', 'Hobbies & Crafts'),
        ('geocaching', 'Geocaching & Treasure Hunting'),
        ('urban_exploration', 'Urban Exploration'),
        ('biking', 'Biking & Cycling'),
        ('rock_climbing', 'Rock Climbing & Adventure Sports'),
        ('extreme_sports', 'Extreme Sports'),
        ('stand_up_paddleboarding', 'Stand-Up Paddleboarding'),
        ('skateboarding', 'Skateboarding'),
        ('motorsports', 'Motorsports & Racing'),
        ('horse_racing', 'Horse Racing & Equestrian Sports'),
        ('snow_sports', 'Snow Sports'),
        ('space_technology', 'Space Technology & Exploration'),
        ('sustainable_farming', 'Sustainable Farming'),
        ('urban_farming', 'Urban Farming & Gardening'),
        ('composting', 'Composting & Waste Management'),
        ('ecotourism', 'Ecotourism & Sustainable Travel'),
        ('green_living', 'Green Living & Sustainability'),
    ]

    COUNTRY_CHOICES = [
        ('NG', 'Nigeria'),
    ]

    STATE_CHOICES = [
        ("All", 'All'),
        ("Abia", "Abia"), ("Adamawa", "Adamawa"), ("Akwa Ibom", "Akwa Ibom"),
        ("Anambra", "Anambra"), ("Bauchi", "Bauchi"), ("Bayelsa", "Bayelsa"),
        ("Benue", "Benue"), ("Borno", "Borno"), ("Cross River", "Cross River"),
        ("Delta", "Delta"), ("Ebonyi", "Ebonyi"), ("Edo", "Edo"), ("Ekiti", "Ekiti"),
        ("Enugu", "Enugu"), ("Gombe", "Gombe"), ("Imo", "Imo"), ("Jigawa", "Jigawa"),
        ("Kaduna", "Kaduna"), ("Kano", "Kano"), ("Katsina", "Katsina"), ("Kebbi", "Kebbi"),
        ("Kogi", "Kogi"), ("Kwara", "Kwara"), ("Lagos", "Lagos"), ("Nasarawa", "Nasarawa"),
        ("Niger", "Niger"), ("Ogun", "Ogun"), ("Ondo", "Ondo"), ("Osun", "Osun"),
        ("Oyo", "Oyo"), ("Plateau", "Plateau"), ("Rivers", "Rivers"), ("Sokoto", "Sokoto"),
        ("Taraba", "Taraba"), ("Yobe", "Yobe"), ("Zamfara", "Zamfara"), ("Abuja", "Abuja")
    ]

    CITY_CHOICES = [
        ("All", 'All'),
        ("Aba", "Aba"), ("Umuahia", "Umuahia"),
        ("Yola", "Yola"), ("Mubi", "Mubi"),
        ("Uyo", "Uyo"), ("Eket", "Eket"),
        ("Awka", "Awka"), ("Onitsha", "Onitsha"), ("Nnewi", "Nnewi"),
        ("Bauchi", "Bauchi"), ("Azare", "Azare"),
        ("Yenagoa", "Yenagoa"),
        ("Makurdi", "Makurdi"), ("Otukpo", "Otukpo"),
        ("Maiduguri", "Maiduguri"), ("Biu", "Biu"),
        ("Calabar", "Calabar"), ("Ikom", "Ikom"),
        ("Warri", "Warri"), ("Asaba", "Asaba"), ("Sapele", "Sapele"),
        ("Abakaliki", "Abakaliki"),
        ("Benin City", "Benin City"), ("Auchi", "Auchi"),
        ("Ado Ekiti", "Ado Ekiti"),
        ("Enugu", "Enugu"), ("Nsukka", "Nsukka"),
        ("Gombe", "Gombe"),
        ("Owerri", "Owerri"), ("Orlu", "Orlu"),
        ("Dutse", "Dutse"),
        ("Kaduna", "Kaduna"), ("Zaria", "Zaria"),
        ("Kano", "Kano"), ("Wudil", "Wudil"),
        ("Katsina", "Katsina"), ("Funtua", "Funtua"),
        ("Birnin Kebbi", "Birnin Kebbi"),
        ("Lokoja", "Lokoja"), ("Anyigba", "Anyigba"),
        ("Ilorin", "Ilorin"), ("Offa", "Offa"),
        ("Ikeja", "Ikeja"), ("Badagry", "Badagry"), ("Epe", "Epe"), ("Ikorodu", "Ikorodu"), ("Surulere", "Surulere"),
        ("Lafia", "Lafia"), ("Keffi", "Keffi"),
        ("Minna", "Minna"), ("Bida", "Bida"),
        ("Abeokuta", "Abeokuta"), ("Sagamu", "Sagamu"),
        ("Akure", "Akure"), ("Ondo", "Ondo"),
        ("Osogbo", "Osogbo"), ("Ile Ife", "Ile Ife"),
        ("Ibadan", "Ibadan"), ("Ogbomoso", "Ogbomoso"),
        ("Jos", "Jos"),
        ("Port Harcourt", "Port Harcourt"), ("Bonny", "Bonny"),
        ("Sokoto", "Sokoto"),
        ("Jalingo", "Jalingo"),
        ("Damaturu", "Damaturu"), ("Potiskum", "Potiskum"),
        ("Gusau", "Gusau"),
        ("Garki", "Garki"), ("Maitama", "Maitama"), ("Wuse", "Wuse")
    ]

    STATUS_CHOICES = [
        ('pending', 'Pending Payment'),
        ('published', 'Published'),
    ]

    category = models.CharField(max_length=30, choices=CATEGORY_CHOICES)
    country = models.CharField(max_length=2, choices=COUNTRY_CHOICES, default='NG')
    state = models.CharField(max_length=20, choices=STATE_CHOICES)
    city = models.CharField(max_length=50)  # Cities will be dynamically populated in forms
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')

    class Meta:
        ordering = ['state', 'category']

    def __str__(self):
        return f"{self.get_category_display()} - {self.state} - {self.city}"

    def get_city_choices(self):
        """Returns the list of cities based on the selected state."""

        return self.CITY_CHOICES.get(self.state, [])
# https://youtu.be/H904uD-kGjA?si=hLvC1uWQIF5yHgMF
# ===========================
#  PRODUCTS MODEL
# ===========================
class Products(models.Model):
    product_name = models.CharField(max_length=100)
    product_image = models.ImageField(upload_to='product_images/')
    product_description = models.TextField(max_length=250)
    product_price = models.PositiveIntegerField()
    product_category = models.CharField(max_length=50, choices=LocationCategory.CATEGORY_CHOICES, default="all")
    product_country = models.CharField(max_length=50, choices=LocationCategory.COUNTRY_CHOICES, default="All")
    product_state = models.CharField(max_length=50, choices=LocationCategory.STATE_CHOICES, default="All")
    product_status = models.CharField(max_length=20, choices=LocationCategory.STATUS_CHOICES, default='pending')
    product_city = models.CharField(max_length=50, choices=LocationCategory.CITY_CHOICES, default="All")
    product_brand = models.CharField(max_length=200)
    # product_provider_email = models.CharField(max_length=1000, null=True, blank=True)
    product_provider_phone = models.CharField(max_length=15, null=True, blank=True)
    is_paid = models.BooleanField(default=False)  # Track payment status

    def average_rating(self):
        ratings = self.product_ratings.all()
        if ratings.exists():
            return round(sum(r.rating for r in ratings) / ratings.count(), 1)
        return 0

    def rating_count(self):
        return self.product_ratings.count()

    def __str__(self):
        return f"{self.product_name} - {self.product_city}, {self.product_state}, {self.product_country}"  # Fixed undefined attribute


# ===========================
#  SERVICES MODEL
# ===========================
class Services(models.Model):
    service_name = models.CharField(max_length=100)
    service_image = models.ImageField(upload_to='services_images/')
    service_description = models.TextField(max_length=250)
    service_category = models.CharField(max_length=50, choices=LocationCategory.CATEGORY_CHOICES, default="all")
    service_country = models.CharField(max_length=50, choices=LocationCategory.COUNTRY_CHOICES, default="All")
    service_state = models.CharField(max_length=50, choices=LocationCategory.STATE_CHOICES, default="All")
    service_city = models.CharField(max_length=50, choices=LocationCategory.CITY_CHOICES, default="All")

    service_provider_name = models.CharField(max_length=200)
    service_provider_expertise = models.TextField(max_length=500)
    service_provider_experience_year = models.PositiveIntegerField(null=True, blank=True)
    service_provider_email = models.CharField(max_length=1000)
    service_provider_phone = models.CharField(max_length=15)

    service_status = models.CharField(max_length=20, choices=LocationCategory.STATUS_CHOICES, default='pending')

    other_service_a = models.CharField(max_length=50, blank=True, null=True)
    other_service_b = models.CharField(max_length=50, blank=True, null=True)
    other_service_c = models.CharField(max_length=50, blank=True, null=True)

    is_paid = models.BooleanField(default=False)  # Track payment status

    def average_rating(self):
        ratings = self.service_ratings.all()
        if ratings.exists():
            return round(sum(r.rating for r in ratings) / ratings.count(), 1)
        return 0

    def rating_count(self):
        return self.service_ratings.count()

    def __str__(self):
        return f"{self.service_name} - {self.service_city}, {self.service_state}, {self.service_country}"  # Fixed undefined attribute


# ===========================
#  PRODUCT RATING MODEL
# ===========================
class ProductRating(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE, related_name="product_ratings")
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) # custom user authentication
    rating = models.DecimalField(max_digits=2, decimal_places=1, choices=[(i/2, str(i/2)) for i in range(0, 11)])
    review = models.TextField(max_length=500, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('product', 'user')

    def __str__(self):
        return f"{self.user.username} - {self.rating}⭐ for {self.product.product_name}"


# ===========================
#  SERVICE RATING MODEL
# ===========================
class ServiceRating(models.Model):
    service = models.ForeignKey(Services, on_delete=models.CASCADE, related_name="service_ratings")
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) # custom user authentication
    rating = models.DecimalField(max_digits=2, decimal_places=1, choices=[(i/2, str(i/2)) for i in range(0, 11)])
    review = models.TextField(max_length=500, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('service', 'user')

    def __str__(self):
        return f"{self.user.username} - {self.rating}⭐ for {self.service.service_name}"