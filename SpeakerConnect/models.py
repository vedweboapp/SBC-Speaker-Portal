from django.db import models
from django.contrib.auth.hashers import make_password
from enum import Enum


# Create your models here.
class Person(models.Model):
    email = models.CharField(max_length=255, unique=True, )
    username = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    biography = models.OneToOneField('Biography', on_delete=models.CASCADE, related_name='person_biography')
    topic_descriptions = models.ForeignKey('TopicDescription', on_delete=models.CASCADE, related_name='person_topic_descriptions')
    testimonials = models.ForeignKey('Testimonial', on_delete=models.CASCADE, related_name='person_testimonials')
    images = models.ForeignKey('Images', on_delete=models.CASCADE, related_name='person_image')
    video = models.ForeignKey('Video', on_delete=models.CASCADE, related_name='person_video')
    podcasts = models.ForeignKey('Podcast', on_delete=models.CASCADE, related_name='person_podcasts')
    books = models.ForeignKey('Book', on_delete=models.CASCADE, related_name='books_author')
    media_mentions = models.ForeignKey('MediaMention', on_delete=models.CASCADE, related_name='person_media_mentions')
    white_papers_case_studies = models.ForeignKey('WhitePaperCaseStudy', on_delete=models.CASCADE, related_name='person_white_papers_case_studies')
    degree_files = models.ForeignKey('DegreesCertificatesAwards', on_delete=models.CASCADE, related_name='person_degree_file')
    speaker_contact_information = models.OneToOneField('SpeakerContactInformation', on_delete=models.CASCADE, related_name='person_speaker_contact_information')
    manager_or_teammate = models.OneToOneField('ManagerOrTeammate', on_delete=models.CASCADE, related_name='person_manager_or_teammate')
    social_media_personal = models.OneToOneField('SocialMediaPersonal', on_delete=models.CASCADE, related_name='person_social_media_personal')
    business_info = models.OneToOneField('BusinessInfo', on_delete=models.CASCADE, related_name='business_info_person')
    social_media_business = models.OneToOneField('SocialMediaBusiness', on_delete=models.CASCADE, related_name='person_social_media_business')
    brand_campaignstheme1 = models.ForeignKey('BrandCampaignOrganizationtheme1', on_delete=models.CASCADE, related_name='person_brand_campaignstheme1')
    brand_campaignstheme2 = models.ForeignKey('BrandCampaignOrganizationtheme2', on_delete=models.CASCADE, related_name='person_brand_campaignstheme2')
    at_events = models.OneToOneField('AtEvents', on_delete=models.CASCADE, related_name='at_events_person')
    help_us_book_you = models.OneToOneField('HelpUsBookYou', on_delete=models.CASCADE, related_name='person_help_us_book_you')
    help_us_work_with_you = models.OneToOneField('HelpUsWorkWithYou', on_delete=models.CASCADE, related_name='person_help_us_work_with_you')
    fees = models.OneToOneField('Fees', on_delete=models.CASCADE, related_name='person_fees')
    speaker_pitches = models.ForeignKey('SpeakerPitch', on_delete=models.CASCADE, related_name='person_speaker_pitches')
    previous_clients = models.ForeignKey('PreviousClient', on_delete=models.CASCADE, related_name='person_previous_clients')

    def save(self, *args, **kwargs):
        # Hash the password before saving the object
        if self.password:
            self.password = make_password(self.password)
        super().save(*args, **kwargs)

speaker_topic_enum_dict = {
    'Accessibility': 'accessibility',
    'Adaptability__amp_Agility': 'adaptability_amp_agility',
    'Addictions__amp_Substance_Abuse': 'addictions_amp_substance_abuse',
    'Alliances__amp_Partnerships': 'alliances_amp_partnerships',
    'Artificial_Intelligence_AI': 'artificial_intelligenceAI',
    'Big_Data': 'bigdata',
    'Blockchain__amp_Metaverse': 'blockchain_amp_metaverse',
    'Bullying_At_Work': 'bullyingatwork',
    'Burnout_Prevention': 'burnoutprevention',
    'Business__amp_Corporate': 'business_amp_corporate',
    'Business_Ethics__amp_Values': 'business_ethics_amp_values',
    'Business_Growth': 'businessgrowth',
    'Business_Leadership': 'business_leadership',
    'Business_Management': 'business_management',
    'Business_Technology': 'business_technology',
    'Business_Transitions': 'business_transitions',
    'Change_Management': 'change_management',
    'Collaboration': 'collaboration',
    'Communications': 'communications',
    'Conflict_Resolution': 'conflict_resolution',
    'Consumer_Behaviour__amp_Retail': 'consumer_behaviour_amp_retail',
    'Corporate_Responsibility_CSR': 'corporate_responsibility_CSR',
    'Cultural_Diversity': 'cultural_diversity',
    'Customer_service': 'customer_service',
    'Cyber_Security': 'cyber_security',
    'Digital_marketing': 'digital_marketing',
    'Disability': 'disability',
    'Disruption_Management': 'disruption_management',
    'Disruptive_Innovation': 'disruptive_innovation',
    'Diversity__amp_Inclusion': 'Diversity_amp_inclusion',
    'Economics': 'economics',
    'Emotional_Intelligence': 'emotional_intelligence',
    'Employee_Engagement': 'employee_engagement',
    'Employee_Management': 'employee_management',
    'Employee_Retention': 'employee_retention',
    'Entrepreneurship': 'entrepreneurship',
    'Excellence__amp_Success': 'Excellence_amp_success',
    'Future_of_Work': 'future_of_work',
    'Future_Trends': 'future_trends',
    'Futurists': 'futurists',
    'Gender_Equality': 'gender_equality',
    'Generations_At_Work': 'generations_at_work',
    'Genrational_Differences': 'genrational_differences',
    'Global_Business_Solutions': 'global_business_solutions',
    'Happiness__amp_Positivity': 'happiness_amp_positivity',
    'Health__amp_Human_Performance': 'health_amp_human_performance',
    'Health__amp_Wellness': 'health_amp_wellness',
    'HR__amp_Corporate_Culture': 'hr_amp_corporate_culture',
    'Humour_At_Workplace': 'humour_at_workplace',
    'Inclusive_Leadership': 'inclusive_leadership',
    'Indigenous': 'indigenous',
    'Influence__amp_Negotiation': 'influence_amp_negotiation',
    'Innovation__amp_Creativity': 'innovation_amp_creativity',
    'Inter_Generational_Workplace': 'inter_generational_workplace',
    'Leadership': 'leadership',
    'Leadership__amp_Change': 'leadership_amp_change',
    'Leadership_Development': 'leadership_development',
    'LGBTQ2S': 'LGBTQ2S+',
    'Marketing__amp_Branding': 'marketing_amp_branding',
    'Memory_networking': 'memory_networking',
    'Mental_Health': 'mental_health',
    'Mentoring_At_Work': 'mentoring_at_work',
    'Mergers__amp_Acquisitions': 'mergers_amp_acquisitions',
    'Mindfulness': 'mindfulness',
    'Mindset__amp_Attitude': 'mindset_amp_attitude',
    'Mindset__amp_Goal_Accomplishment': 'mindset_amp_goal_accomplishment',
    'Neurodiversity': 'neurodiversity',
    'Nutrition__amp_Fitness': 'nutrition_amp_fitness',
    'Organizational_Change': 'organizational_change',
    'Organizational_Leadership': 'organizational_leadership',
    'Peak_Performance': 'peak_performance',
    'Personal_Growth': 'personal_growth',
    'Personal_Leadership': 'personal_leadership',
    'Positive_Psychology': 'positive_psychology',
    'Presentation_Skills': 'presentation_skills',
    'Privacy': 'privacy',
    'Process__amp_Systems': 'process_amp_systems',
    'Project_Management': 'project_management',
    'Psychological_Safety': 'psychological_safety',
    'PTSD__amp_Trauma': 'ptsd_amp_trauma',
    'Public_Relations': 'public_relations',
    'Purposeful_Work': 'purposeful_work',
    'Racial_Justice': 'racial_justice',
    'Resilience__amp_Adversity': 'resilience_amp_adversity',
    'Resilience__amp_Change': 'resilience_amp_change',
    'Sales': 'sales',
    'Self_Improvement__amp_Self_Care': 'self_improvement_amp_self_care',
    'Small_Business_Development': 'small_business_development',
    'Social_media': 'social_media',
    'Soft_Skills_Development': 'soft_skills_development',
    'STEM': 'stem',
    'Strategic_thinking': 'strategic_thinking',
    'Stress_Management': 'stress_management',
    'Suicide_Prevention': 'suicide_prevention',
    'Talent_Management': 'talent_management',
    'Teamwork': 'teamwork',
    'Tech_trends': 'tech_trends',
    'Time_Management': 'time_management',
    'Transformation': 'transformation',
    'Trust_Relationships': 'trust_relationships',
    'Unconscious_Bias': 'unconscious_bias',
    'Women_In_Business': 'women_in_business',
    'Women_Of_Influence': 'women_of_influence',
    'Womens_Leadership': 'womens_leadership',
    'Womens_Rights__amp_MeToo': 'womens_rights_amp_metoo',
    'Work_Life_Balance': 'work_life_balance',
    'Workplace_Culture': 'workplace_culture'
}


class SpeakerTopic(models.Model):
    topic = models.CharField(max_length=100, choices=[(key, value) for key, value in speaker_topic_enum_dict.items()])

    @classmethod
    def add_speaker_topic(cls, topic):
        if topic not in speaker_topic_enum_dict:
            print(f"Topic '{topic}' is not a valid option.")
            return

        if not cls.objects.filter(topic=topic).exists():
            cls.objects.create(topic=topic)
        else:
            print(f"Topic '{topic}' already exists.")


class Biography(models.Model):
    highlight = models.TextField()
    long_bio = models.TextField()
    sort_bio = models.TextField()
    speaker_topics_additional_keywords = models.TextField()
    descriptive_title_type = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    province_state = models.CharField(max_length=255)
    microphonetext = models.TextField()
    microphone = models.BinaryField()  # Or use FileField if saving files
    microphone_name = models.CharField(max_length=255)
    speaker_topics = models.ManyToManyField('SpeakerTopic', related_name='speaker_topics')
    speaker_tags = models.ManyToManyField('SpeakerTag', related_name='speaker_tags')
    descriptive_titles = models.ManyToManyField('DescriptiveTitles', related_name='descriptive_titles')
    person = models.ForeignKey('Person', on_delete=models.CASCADE, related_name='biographies')

    def __str__(self):
        return f"Biography - {self.id}"
    
class SpeakerTag(models.Model):
    class TagChoices(models.TextChoices):
        REACT_JS = 'reactjs', 'ReactJs'
        HTML = 'html', 'Html'
        JAVA = 'java', 'Java'
        PYTHON = 'python', 'Python'

    tag = models.CharField(max_length=50, choices=TagChoices.choices)

    def __str__(self):
        return self.tag
    
    
class DescriptiveTitles(models.Model):
    title = models.CharField(max_length=255, unique=True) 

    def __str__(self):
        return self.title

class TopicDescription(models.Model):
    title = models.CharField(max_length=255)
    body_text = models.TextField()
    delivered_as = models.CharField(max_length=255)
    audio_clip = models.BinaryField()  # Or use FileField if saving files
    audio_clip_name = models.CharField(max_length=255)
    audiotext = models.TextField()
    video_clip = models.CharField(max_length=255)

    # Define a foreign key relationship with Person
    person = models.ForeignKey('Person', on_delete=models.CASCADE, related_name='topic_descriptions_person')

    def __str__(self):
        return self.title
    
class Testimonial(models.Model):
    organizer_name = models.CharField(max_length=255)
    organization_name = models.CharField(max_length=255)
    link_to_video = models.CharField(max_length=255)

    # Define a foreign key relationship with Person
    person = models.ForeignKey('Person', on_delete=models.CASCADE, related_name='testimonials_person')

    def __str__(self):
        return f"{self.organizer_name}'s Testimonial for {self.person.username}"
    
class Images(models.Model):
    image_data = models.BinaryField()
    image_name = models.CharField(max_length=255)
    cropped_image_data = models.BinaryField()
    cropped_image_name = models.CharField(max_length=255)
    own_right = models.BooleanField(default=False)
    sbc_permission = models.BooleanField(default=False)

    # Define a foreign key relationship with Person
    person = models.ForeignKey('Person', on_delete=models.CASCADE, related_name='person_images')

    def __str__(self):
        return self.image_name

class Video(models.Model):
    title = models.CharField(max_length=100)
    link = models.CharField(max_length=200)
    hd_quality = models.BooleanField(default=False)
    own_rights = models.BooleanField(default=False)
    grant_permission = models.BooleanField(default=False)
    reason = models.CharField(max_length=200, null=True, blank=True)

    # Define a foreign key relationship with Person
    person = models.ForeignKey('Person', on_delete=models.CASCADE, related_name='video_person')

    def __str__(self):
        return self.title


class Podcast(models.Model):
    title = models.CharField(max_length=255)
    link = models.CharField(max_length=255)
    source = models.CharField(max_length=255)

    # Define a foreign key relationship with Person
    person = models.ForeignKey('Person', on_delete=models.CASCADE, related_name='podcasts_person')

    def __str__(self):
        return self.title


class Book(models.Model):
    upload_book_image = models.BinaryField()
    book_name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=1000)
    authors = models.CharField(max_length=255)
    publisher = models.CharField(max_length=255)
    link = models.CharField(max_length=255)
    cost_per_book_cad = models.CharField(max_length=255)
    bulk_order_purchase_offered = models.BooleanField()
    price_per_book_cad = models.CharField(max_length=255)
    number_of_books = models.IntegerField()

    # Define a foreign key relationship with Person
    person = models.ForeignKey('Person', on_delete=models.CASCADE, related_name='person_book')

    def __str__(self):
        return self.book_name


class MediaMention(models.Model):
    organization_name = models.CharField(max_length=255)
    interview_article_title = models.CharField(max_length=255)
    link = models.CharField(max_length=255)
    date = models.CharField(max_length=255)
    interview_source_name = models.CharField(max_length=255)

    # Define foreign key relationship with Person
    person = models.ForeignKey('Person', on_delete=models.CASCADE, related_name='media_mentions_person')

    def __str__(self):
        return self.interview_article_title

class WhitePaperCaseStudy(models.Model):
    organization_name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    topics = models.CharField(max_length=255)
    description = models.TextField()
    link = models.CharField(max_length=255)
    date = models.DateField()

    # Define foreign key relationship with Person
    person = models.ForeignKey('Person', on_delete=models.CASCADE, related_name='white_papers_case_studies_persons')

    def __str__(self):
        return self.title

class DegreesCertificatesAwards(models.Model):
    degree_data = models.BinaryField()
    degreescertificatesawards_name = models.CharField(max_length=255)
    
    person = models.ForeignKey('Person', on_delete=models.CASCADE, related_name='person_degree_files')

    def __str__(self):
        return self.degreescertificatesawards_name


class SpeakerContactInformation(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    middle_initials = models.CharField(max_length=10)
    secondary_names_nick_name = models.CharField(max_length=50)
    pronouns = models.CharField(max_length=50)
    cell_phone = models.CharField(max_length=20)
    main_email = models.CharField(max_length=100)
    website_link = models.CharField(max_length=200)
    rss_blog_link = models.CharField(max_length=200)
    rss_blog_link_2 = models.CharField(max_length=200)
    closest_major_airport = models.CharField(max_length=50)
    person = models.ForeignKey('Person', on_delete=models.CASCADE, related_name='speaker_contact_information_person')

class ManagerOrTeammate(models.Model):
    assist_coordinating = models.BooleanField()
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    pronouns = models.CharField(max_length=50)
    cell_phone = models.CharField(max_length=20)
    main_email = models.CharField(max_length=100)
    website = models.CharField(max_length=200)
    person = models.ForeignKey('Person', on_delete=models.CASCADE, related_name='manager_or_teammate_person')

class SocialMediaPersonal(models.Model):
    facebook_link = models.CharField(max_length=200)
    facebook_handle = models.CharField(max_length=50)
    facebook_followers = models.CharField(max_length=50)
    instagram_link = models.CharField(max_length=200)
    instagram_handle = models.CharField(max_length=50)
    instagram_followers = models.CharField(max_length=50)
    twitter_link = models.CharField(max_length=200)
    twitter_handle = models.CharField(max_length=50)
    twitter_followers = models.CharField(max_length=50)
    linkedin_link = models.CharField(max_length=200)
    linkedin_handle = models.CharField(max_length=50)
    linkedin_followers = models.CharField(max_length=50)
    tiktok_link = models.CharField(max_length=200)
    tiktok_handle = models.CharField(max_length=50)
    tiktok_followers = models.CharField(max_length=50)
    person = models.ForeignKey('Person', on_delete=models.CASCADE, related_name='social_media_personal_person')


class BusinessInfo(models.Model):
    issue_payment = models.BooleanField()
    official_business_name = models.CharField(max_length=100)
    business_email = models.CharField(max_length=100)
    business_phone = models.CharField(max_length=15)
    business_number = models.CharField(max_length=20)
    website = models.CharField(max_length=200)
    person = models.ForeignKey('Person', on_delete=models.CASCADE, related_name='person_business_info')

class SocialMediaBusiness(models.Model):
    facebook_link = models.CharField(max_length=200)
    facebook_handle = models.CharField(max_length=50)
    facebook_followers = models.CharField(max_length=50)
    instagram_link = models.CharField(max_length=200)
    instagram_handle = models.CharField(max_length=50)
    instagram_followers = models.CharField(max_length=50)
    twitter_link = models.CharField(max_length=200)
    twitter_handle = models.CharField(max_length=50)
    twitter_followers = models.CharField(max_length=50)
    linkedin_link = models.CharField(max_length=200)
    linkedin_handle = models.CharField(max_length=50)
    linkedin_followers = models.CharField(max_length=50)
    tiktok_link = models.CharField(max_length=200)
    tiktok_handle = models.CharField(max_length=50)
    tiktok_followers = models.CharField(max_length=50)
    person = models.ForeignKey('Person', on_delete=models.CASCADE, related_name='social_media_business_person')

class BrandCampaignOrganizationtheme1(models.Model):
    part_of_social_media = models.BooleanField()
    organization_name = models.CharField(max_length=255)
    platforms = models.CharField(max_length=255)
    link_to_campaign = models.CharField(max_length=255)
    start_year = models.CharField(max_length=4)
    end_year = models.CharField(max_length=4)
    person = models.ForeignKey('Person', on_delete=models.CASCADE)

class BrandCampaignOrganizationtheme2(models.Model):
    part_of_social_media = models.BooleanField()
    organization_name = models.CharField(max_length=255)
    platforms = models.CharField(max_length=255)
    link_to_campaign = models.CharField(max_length=255)
    start_year = models.CharField(max_length=4)
    end_year = models.CharField(max_length=4)
    person = models.ForeignKey('Person', on_delete=models.CASCADE)

class AtEvents(models.Model):
    using_presentation_software = models.BooleanField()
    presentation_software_name = models.CharField(max_length=255)
    using_audience_interaction_software = models.BooleanField()
    audience_interaction_software_name = models.CharField(max_length=255)
    attending_sessions_before_after_presentation = models.BooleanField()
    attending_meals_networking_sessions = models.BooleanField()
    dietary_requirements_restrictions = models.CharField(max_length=255)
    A_V_requirements = models.CharField(max_length=255)
    prefer_to_book_travel = models.CharField(max_length=255)
    prefer_to_book_travel = models.BooleanField()
    use_travel_agent = models.BooleanField()
    Preferred_Seating = models.CharField(max_length=255)
    Preferred_Airline = models.CharField(max_length=255)
    West_Jet_number = models.CharField(max_length=255)
    Air_Canada_number = models.CharField(max_length=255)
    special_conditions_for_travel_arrangements = models.BooleanField()
    table_for_book_sales = models.BooleanField()
    person = models.ForeignKey('Person', on_delete=models.CASCADE)

class SpeakerIntroduction(models.Model):
    introduction_text = models.CharField(max_length=255)
    at_events = models.ForeignKey(AtEvents, on_delete=models.CASCADE, related_name='speaker_introduction')

class HelpUsBookYou(models.Model):
    speaker_reason_to_work_with = models.CharField(max_length=255)
    value_adds_and_offerings = models.BooleanField()
    books_how_many_items = models.CharField(max_length=255)
    books_value_per_item = models.CharField(max_length=255)
    online_training_how_many_items = models.CharField(max_length=255)
    online_training_value_per_item = models.CharField(max_length=255)
    merch_how_many_items = models.CharField(max_length=255)
    merch_value_per_item = models.CharField(max_length=255)
    merch_2_how_many_items = models.CharField(max_length=255)
    merch_2_value_per_item = models.CharField(max_length=255)
    complementary_virtual_follow_sessions_consultation = models.BooleanField()
    inclusive_of_travel_expenses = models.CharField(max_length=255)
    industries_do_you_not_work_with = models.CharField(max_length=255)
    favorite_audiences_event_types = models.CharField(max_length=255)
    target_audiences_industries = models.CharField(max_length=255)
    English_French = models.BooleanField()
    Q_A_in_French = models.BooleanField()
    offer_recordings = models.BooleanField()
    primary_source_of_income = models.BooleanField()
    hoping_for_speaking_to_become_your_primary_source_income = models.BooleanField()
    current_speak_per_month = models.CharField(max_length=255)
    virtual_events_over_pandemic = models.CharField(max_length=255)
    speak_per_month = models.CharField(max_length=255)
    market_yourself_as_a_speaker = models.CharField(max_length=255)
    affiliated_with_any_other_speakers_agencies = models.CharField(max_length=255)
    percentage_of_bookings = models.CharField(max_length=255)
    Approximately_what_percentage = models.CharField(max_length=255)
    speakers_are_you_affiliated_with = models.CharField(max_length=255)
    person = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='help_us_book_you_person')


class HelpUsWorkWithYou(models.Model):
    newsletter_onboarding = models.CharField(max_length=255)
    tracking_system = models.BooleanField()
    whatsapp = models.BooleanField()
    business_ownership = models.BooleanField()
    crm_usage = models.CharField(max_length=255)
    appointment_booking_software = models.CharField(max_length=255)
    expectations_with_sbc = models.CharField(max_length=255)
    something_about_you = models.CharField(max_length=255)
    stories = models.CharField(max_length=255)
    person = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='help_us_work_with_you_person')


class Fees(models.Model):
    Pro_Bono_Events = models.CharField(max_length=255)
    Corporate_Keynote_20_60_Minutes = models.CharField(max_length=255)
    Corporate_Workshop_60_120_Minutes = models.CharField(max_length=255)
    Corporate_Half_Day_Training_or_Keynote_Breakout = models.CharField(max_length=255)
    Corporate_Full_Day_Training = models.CharField(max_length=255)
    Concurrent_Sessions_Fee = models.CharField(max_length=255)
    One_Session_in_the_Morning_Fee = models.CharField(max_length=255)
    One_Session_in_the_Afternoon_Fee = models.CharField(max_length=255)
    Multiple_Sessions_on_Concurrent_Days = models.CharField(max_length=255)
    Multiple_Sessions_Over_a_Period_of_Time = models.CharField(max_length=255)
    Lowest_Acceptance_for_Informal_Talk = models.CharField(max_length=255)
    One_Day_Event = models.CharField(max_length=255)
    One_Day_Plus_Evening_Ceremony_Keynote = models.CharField(max_length=255)
    Two_Day_Event = models.CharField(max_length=255)
    Two_Day_Plus_Evening_Ceremony_Keynote = models.CharField(max_length=255)
    Three_Day_Event = models.CharField(max_length=255)
    Three_Day_Plus_Evening_Ceremony_Keynote = models.CharField(max_length=255)
    Four_Day_Event = models.CharField(max_length=255)
    Four_Day_Plus_Evening_Ceremony_Keynote = models.CharField(max_length=255)
    What_is_your_corporate_speaker_fee = models.CharField(max_length=255)
    lowest_you_will_accept = models.CharField(max_length=255)
    limitations_or_condition = models.CharField(max_length=255)
    Driving_Distance_Fee = models.CharField(max_length=255)
    Province_Fee = models.CharField(max_length=255)
    Western_Canada_Fee = models.CharField(max_length=255)
    Eastern_Canada_Fee = models.CharField(max_length=255)
    Northern_Canada_Fee = models.CharField(max_length=255)
    Remote_Location_Fee = models.CharField(max_length=255)
    Local_Discount = models.BooleanField()
    Local_Fee = models.CharField(max_length=255)
    Client_Direct_Approach_for_Local_Event = models.CharField(max_length=255)
    Virtual_Discount = models.BooleanField()
    Virtual_Fee = models.CharField(max_length=255)
    Client_Direct_Approach_for_Virtual_Event = models.CharField(max_length=255)
    Small_Audience_Discount = models.BooleanField()
    Small_Audience_Fee = models.CharField(max_length=255)
    Client_Direct_Approach_for_Small_Audience_Event = models.CharField(max_length=255)
    Qualification_for_Small_Audience = models.CharField(max_length=255)
    Nonprofit_Discount = models.BooleanField()
    Nonprofit_Fee = models.CharField(max_length=255)
    Client_Direct_Approach_for_Nonprofit = models.CharField(max_length=255)
    Charitable_Organization_Discount = models.BooleanField()
    Charitable_Fee = models.CharField(max_length=255)
    Client_Direct_Approach_for_Charitable_Organization = models.CharField(max_length=255)
    outside_of_speaker_fee_ranges = models.CharField(max_length=255)
    Rate_Increase = models.BooleanField()
    person = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='person_fee')

    class Meta:
        verbose_name_plural = 'Fees'

class SpeakerPitch(models.Model):
    general_pitch = models.CharField(max_length=255)
    keyword_topic_focus_pitch = models.CharField(max_length=255)
    Short_pitch_up = models.CharField(max_length=255)
    person = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='speaker_pitches_person')

    class Meta:
        verbose_name_plural = 'SpeakerPitches'

class PreviousClient(models.Model):
    organization_name = models.CharField(max_length=255)
    person = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='previous_clients_person')

    class Meta:
        verbose_name_plural = 'PreviousClients'