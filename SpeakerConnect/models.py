# from passlib.hash import bcrypt

from django.db import models
import bcrypt
from django.contrib.auth.hashers import make_password, check_password


class Person(models.Model):
    email = models.CharField(max_length=255, unique=True)
    username = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)

    def save(self, *args, **kwargs):
        if self.password:
            self.set_password(self.password)
        super().save(*args, **kwargs)

    def set_password(self, raw_password):
        # Hash and set the password
        self.password = make_password(raw_password)


    # speaker_contact_information = models.OneToOneField('SpeakerContactInformation', on_delete=models.CASCADE, related_name='person_speaker_contact_information',null=True,blank=True)
    # manager_or_teammate = models.OneToOneField('ManagerOrTeammate', on_delete=models.CASCADE, related_name='person_manager_or_teammate',null=True,blank=True)
    # social_media_personal = models.OneToOneField('SocialMediaPersonal', on_delete=models.CASCADE, related_name='person_social_media_personal',null=True,blank=True)
    # biography = models.OneToOneField('Biography', on_delete=models.CASCADE, related_name='person_biography',null=True,blank=True)
    # topic_descriptions = models.ManyToManyField('TopicDescription', related_name='person_topic_descriptions')
    # # testimonials = models.ForeignKey('Testimonial', on_delete=models.CASCADE, related_name='person_testimonials')
    # images = models.ForeignKey('Images', on_delete=models.CASCADE, related_name='person_image',null=True,blank=True)
    # # video = models.ForeignKey('Video', on_delete=models.CASCADE, related_name='person_video')
    # # podcasts = models.ForeignKey('Podcast', on_delete=models.CASCADE, related_name='person_podcasts')
    # books = models.ManyToManyField('Book', related_name='books_author', null=True, blank=True)
    # # media_mentions = models.ForeignKey('MediaMention', on_delete=models.CASCADE, related_name='person_media_mentions')
    # white_papers_case_studies = models.ManyToManyField('WhitePaperCaseStudy', related_name='person_white_papers_case_studies')
    # degree_files = models.ForeignKey('DegreesCertificatesAwards', on_delete=models.CASCADE, related_name='person_degree_file')
    # speaker_contact_information = models.OneToOneField('SpeakerContactInformation', on_delete=models.CASCADE, related_name='person_speaker_contact_information')
    # manager_or_teammate = models.OneToOneField('ManagerOrTeammate', on_delete=models.CASCADE, related_name='person_manager_or_teammate')
    # social_media_personal = models.OneToOneField('SocialMediaPersonal', on_delete=models.CASCADE, related_name='person_social_media_personal')
    # business_info = models.OneToOneField('BusinessInfo', on_delete=models.CASCADE, related_name='business_info_person')
    # social_media_business = models.OneToOneField('SocialMediaBusiness', on_delete=models.CASCADE, related_name='person_social_media_business')
    # brand_campaignstheme1 = models.ForeignKey('BrandCampaignOrganizationtheme1', on_delete=models.CASCADE, related_name='person_brand_campaignstheme1')
    # brand_campaignstheme2 = models.ForeignKey('BrandCampaignOrganizationtheme2', on_delete=models.CASCADE, related_name='person_brand_campaignstheme2')
    # at_events = models.OneToOneField('AtEvents', on_delete=models.CASCADE, related_name='at_events_person')
    # help_us_book_you = models.OneToOneField('HelpUsBookYou', on_delete=models.CASCADE, related_name='person_help_us_book_you')
    # help_us_work_with_you = models.OneToOneField('HelpUsWorkWithYou', on_delete=models.CASCADE, related_name='person_help_us_work_with_you')
    # fees = models.OneToOneField('Fees', on_delete=models.CASCADE, related_name='person_fees')
    # speaker_pitches = models.ManyToManyField('SpeakerPitch', related_name='person_speaker_pitches')
    # previous_clients = models.ManyToManyField('PreviousClient', related_name='person_previous_clients')

    # def save(self, *args, **kwargs):
    #     # Hash the password before saving the object
    #     if self.password:
    #         self.password = make_password(self.password)
    #     super().save(*args, **kwargs)

class SpeakerTopic(models.Model):
    TOPIC_CHOICES = [
        ('Accessibility', 'accessibility'),
        ('Adaptability & Agility', 'adaptability_amp_agility'),
        ('Addictions & Substance Abuse', 'addictions_amp_substance_abuse'),
        ('Alliances & Partnerships', 'alliances_amp_partnerships'),
        ('Artificial Intelligence (AI)', 'artificial_intelligenceAI'),
        ('Big Data', 'bigdata'),
        ('Blockchain & Metaverse', 'blockchain_amp_metaverse'),
        ('Bullying At Work', 'bullyingatwork'),
        ('Burnout Prevention', 'burnoutprevention'),
        ('Business & Corporate', 'business_amp_corporate'),
        ('Business Ethics & Values', 'business_ethics_amp_values'),
        ('Business Growth', 'businessgrowth'),
        ('Business Leadership', 'business_leadership'),
        ('Business Management', 'business_management'),
        ('Business Technology', 'business_technology'),
        ('Business Transitions', 'business_transitions'),
        ('Change Management', 'change_management'),
        ('Collaboration', 'collaboration'),
        ('Communications', 'communications'),
        ('Conflict Resolution', 'conflict_resolution'),
        ('Consumer Behaviour & Retail', 'consumer_behaviour_amp_retail'),
        ('Corporate Responsibility (CSR)', 'corporate_responsibility_CSR'),
        ('Cultural Diversity', 'cultural_diversity'),
        ('Customer Service', 'customer_service'),
        ('Cyber Security', 'cyber_security'),
        ('Digital Marketing', 'digital_marketing'),
        ('Disability', 'disability'),
        ('Disruption Management', 'disruption_management'),
        ('Disruptive Innovation', 'disruptive_innovation'),
        ('Diversity & Inclusion', 'Diversity_amp_inclusion'),
        ('Economics', 'economics'),
        ('Emotional Intelligence', 'emotional_intelligence'),
        ('Employee Engagement', 'employee_engagement'),
        ('Employee Management', 'employee_management'),
        ('Employee Retention', 'employee_retention'),
        ('Entrepreneurship', 'entrepreneurship'),
        ('Excellence & Success', 'Excellence_amp_success'),
        ('Future of Work', 'future_of_work'),
        ('Future Trends', 'future_trends'),
        ('Futurists', 'futurists'),
        ('Gender Equality', 'gender_equality'),
        ('Generations At Work', 'generations_at_work'),
        ('Generational Differences', 'genrational_differences'),
        ('Global Business Solutions', 'global_business_solutions'),
        ('Happiness & Positivity', 'happiness_amp_positivity'),
        ('Health & Human Performance', 'health_amp_human_performance'),
        ('Health & Wellness', 'health_amp_wellness'),
        ('HR & Corporate Culture', 'hr_amp_corporate_culture'),
        ('Humour At Workplace', 'humour_at_workplace'),
        ('Inclusive Leadership', 'inclusive_leadership'),
        ('Indigenous', 'indigenous'),
        ('Influence & Negotiation', 'influence_amp_negotiation'),
        ('Innovation & Creativity', 'innovation_amp_creativity'),
        ('Inter-Generational Workplace', 'inter_generational_workplace'),
        ('Leadership', 'leadership'),
        ('Leadership & Change', 'leadership_amp_change'),
        ('Leadership Development', 'leadership_development'),
        ('LGBTQ2S+', 'LGBTQ2S+'),
        ('Marketing & Branding', 'marketing_amp_branding'),
        ('Memory Networking', 'memory_networking'),
        ('Mental Health', 'mental_health'),
        ('Mentoring At Work', 'mentoring_at_work'),
        ('Mergers & Acquisitions', 'mergers_amp_acquisitions'),
        ('Mindfulness', 'mindfulness'),
        ('Mindset & Attitude', 'mindset_amp_attitude'),
        ('Mindset & Goal Accomplishment', 'mindset_amp_goal_accomplishment'),
        ('Neurodiversity', 'neurodiversity'),
        ('Nutrition & Fitness', 'nutrition_amp_fitness'),
        ('Organizational Change', 'organizational_change'),
        ('Organizational Leadership', 'organizational_leadership'),
        ('Peak Performance', 'peak_performance'),
        ('Personal Growth', 'personal_growth'),
        ('Personal Leadership', 'personal_leadership'),
        ('Positive Psychology', 'positive_psychology'),
        ('Presentation Skills', 'presentation_skills'),
        ('Privacy', 'privacy'),
        ('Process & Systems', 'process_amp_systems'),
        ('Project Management', 'project_management'),
        ('Psychological Safety', 'psychological_safety'),
        ('PTSD & Trauma', 'ptsd_amp_trauma'),
        ('Public Relations', 'public_relations'),
        ('Purposeful Work', 'purposeful_work'),
        ('Racial Justice', 'racial_justice'),
        ('Resilience & Adversity', 'resilience_amp_adversity'),
        ('Resilience & Change', 'resilience_amp_change'),
        ('Sales', 'sales'),
        ('Self Improvement & Self Care', 'self_improvement_amp_self_care'),
        ('Small Business Development', 'small_business_development'),
        ('Social Media', 'social_media'),
        ('Soft Skills Development', 'soft_skills_development'),
        ('STEM', 'stem'),
        ('Strategic Thinking', 'strategic_thinking'),
        ('Stress Management', 'stress_management'),
        ('Suicide Prevention', 'suicide_prevention'),
        ('Talent Management', 'talent_management'),
        ('Teamwork', 'teamwork'),
        ('Tech Trends', 'tech_trends'),
        ('Time Management', 'time_management'),
        ('Transformation', 'transformation'),
        ('Trust & Relationships', 'trust_relationships'),
        ('Unconscious Bias', 'unconscious_bias'),
        ('Women In Business', 'women_in_business'),
        ('Women Of Influence', 'women_of_influence'),
        ('Women\'s Leadership', 'womens_leadership'),
        ('Women\'s Rights & MeToo', 'womens_rights_amp_metoo'),
        ('Work Life Balance', 'work_life_balance'),
        ('Workplace Culture', 'workplace_culture'),
    ]

    topic = models.CharField(max_length=100, choices=TOPIC_CHOICES)

    def __str__(self):
        return self.topic

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
    descriptive_title_choices = [
    ('academia', 'Academia'),
    ('adventurers', 'Adventurers'),
    ('agriculture__amp_farming', 'Agriculture & Farming'),
    ('all_staff_meeting', 'All Staff Meeting'),
    ('annual_general_meetings', 'Annual General Meetings'),
    ('associations__amp_unions', 'Associations & Unions'),
    ('athletes__amp_sports', 'Athletes & Sports'),
    ('award_galas__amp_after_dinner', 'Award Galas & After Dinner'),
    ('awareness_days', 'Awareness Days'),
    ('bilingual__amp_french', 'Bilingual & French'),
    ('board_meetings__amp_strategic_advisory', 'Board Meetings & Strategic Advisory'),
    ('campus__amp_university_speakers', 'Campus & University Speakers'),
    ('cancer_awareness', 'Cancer Awareness'),
    ('career_development', 'Career Development'),
    ('celebrity', 'Celebrity'),
    ('certified_speakers', 'Certified Speakers'),
    ('certified_speaking_professionals_csp', 'Certified Speaking Professionals CSP'),
    ('charities__amp_foundations', 'Charities & Foundations'),
    ('community_engagement_events', 'Community Engagement Events'),
    ('conference', 'Conference'),
    ('conferences__amp_summits', 'Conferences & Summits'),
    ('consultant__amp_coach', 'Consultant & Coach'),
    ('corporate_audience', 'Corporate Audience'),
    ('corporate_entertainers', 'Corporate Entertainers'),
    ('corporations__amp_businesses', 'Corporations & Businesses'),
    ('department_meeting', 'Department Meeting'),
    ('economic_development', 'Economic Development'),
    ('education__amp_teachers', 'Education & Teachers'),
    ('endorsement__amp_product_launch', 'Endorsement & Product Launch'),
    ('environment__amp_climate_change', 'Environment & Climate Change'),
    ('event_hosts__amp_moderators', 'Event Hosts & Moderators'),
    ('executive_leadership__amp_c_suite', 'Executive Leadership & C-Suite'),
    ('family__amp_parenting', 'Family & Parenting'),
    ('finance__amp_insurance', 'Finance & Insurance'),
    ('first_nation_motivational_speakers', 'First Nation Motivational Speakers'),
    ('first_responders', 'First Responders'),
    ('fundraisers__amp_banquets', 'Fundraisers & Banquets'),
    ('funny__amp_comedy', 'Funny & Comedy'),
    ('government_departments__amp_agencies', 'Government Departments & Agencies'),
    ('guest_panelist__amp_guided_q_ampa', 'Guest Panelist & Guided Q&A'),
    ('hall_of_fame', 'Hall of Fame'),
    ('health_and_safety', 'Health and Safety'),
    ('healthcare', 'Healthcare'),
    ('home__amp_garden', 'Home & Garden'),
    ('hybrid_workplace', 'Hybrid Workplace'),
    ('industry_types', 'Industry Types'),
    ('infrastructure__amp_urban_planning', 'Infrastructure & Urban Planning'),
    ('inspirational', 'Inspirational'),
    ('interactive__amp_experience', 'Interactive & Experience'),
    ('key_note', 'Key Note'),
    ('lifestyle__amp_health', 'Lifestyle & Health'),
    ('managing_remote_employees', 'Managing Remote Employees'),
    ('medical__amp_healthcare', 'Medical & Healthcare'),
    ('men', 'Men'),
    ('mentalists__amp_hypnotists', 'Mentalists & Hypnotists'),
    ('military', 'Military'),
    ('most_requested', 'Most Requested'),
    ('motivation', 'Motivation'),
    ('mountain_climbers', 'Mountain Climbers'),
    ('non_binary', 'Non Binary'),
    ('olympians__amp_olympics', 'Olympians & Olympics'),
    ('opening__amp_closing_keynote', 'Opening & Closing Keynote'),
    ('orateur__amp_conférencier', 'Orateur & Conférencier'),
    ('patient_safety__amp_patient_care', 'Patient Safety & Patient Care'),
    ('philanthropy__amp_giving_back', 'Philanthropy & Giving Back'),
    ('pofessional_development_days_pd_days', 'Professional Development Days PD Days'),
    ('politicians', 'Politicians'),
    ('presentation_formats', 'Presentation Formats'),
    ('real_estate', 'Real Estate'),
    ('research__amp_science', 'Research & Science'),
    ('safety', 'Safety'),
    ('sales_motivation__amp_sales_kick_off', 'Sales Motivation & Sales Kick Off'),
    ('school_boards', 'School Boards'),
    ('scientific__amp_technical', 'Scientific & Technical'),
    ('social__amp_cultural', 'Social & Cultural'),
    ('social_justice__amp_human_rights', 'Social Justice & Human Rights'),
    ('sort_by', 'Sort By'),
    ('speaker_types', 'Speaker Types'),
    ('staff_appreciation__amp_employee_recognition', 'Staff Appreciation & Employee Recognition'),
    ('storytelling', 'Storytelling'),
    ('sustainable_development', 'Sustainable Development'),
    ('ted__amp_tedx', 'TED & TEDx'),
    ('town_halls__amp_retreats', 'Town Halls & Retreats'),
    ('trade_shows__amp_conventions', 'Trade Shows & Conventions'),
    ('Under $5,000', 'Under $5,000'),
    ('virtual__amp_online_meetings', 'Virtual & Online Meetings'),
    ('virtual_engagement', 'Virtual Engagement'),
    ('virtual_speakers', 'Virtual Speakers'),
    ('virtual_teams__amp_remote_workers', 'Virtual Teams & Remote Workers'),
    ('women', 'Women'),
    ('workshop__amp_training', 'Workshop & Training'),
    ('youth_leadership__amp_students', 'Youth Leadership & Students'),
    ('youth_leadership_and_student_empowerment', 'Youth Leadership and Student Empowerment'),
]


    title = models.CharField(
        max_length=255,
        choices=descriptive_title_choices,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.title



class Biography(models.Model):
    highlight = models.TextField()
    long_bio = models.TextField()
    sort_bio = models.TextField()
    speaker_topics_additional_keywords = models.TextField()
    descriptive_title_type = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    province_state = models.CharField(max_length=255)
    microphonetext = models.TextField()
    microphone = models.FileField(upload_to='get_files/')
    microphone_name = models.CharField(max_length=255)
    speaker_topics = models.ManyToManyField(SpeakerTopic, related_name='biographies')
    speaker_tags = models.ManyToManyField(SpeakerTag, related_name='biographies')
    descriptive_titles = models.ManyToManyField(DescriptiveTitles, related_name='biographies')
    person = models.ForeignKey('Person', on_delete=models.CASCADE, related_name='biographies')

    def __str__(self):
        return f"Biography - {self.id}"
    

    
  

class TopicDescription(models.Model):
    title = models.CharField(max_length=255,null=True,blank=True)
    body_text = models.TextField(null=True,blank=True)
    delivered_as = models.CharField(max_length=255,null=True,blank=True)
    audio_clip = models.BinaryField()  # Or use FileField if saving files
    audio_clip_name = models.CharField(max_length=255,null=True,blank=True)
    audiotext = models.TextField(null=True,blank=True)
    video_clip = models.CharField(max_length=255,null=True,blank=True)

    # Define a foreign key relationship with Person
    person = models.ForeignKey('Person', on_delete=models.CASCADE, related_name='topic_descriptions_person',null=True,blank=True)

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
    image_data = models.FileField(upload_to='get_files/')
    image_name = models.CharField(max_length=255)
    cropped_image_data = models.FileField(upload_to='get_files/')
    cropped_image_name = models.CharField(max_length=255)
    own_right = models.BooleanField(default=False)
    sbc_permission = models.BooleanField(default=False)

    # Define a foreign key relationship with Person
    person = models.ForeignKey('Person', on_delete=models.CASCADE, related_name='person_images',null=True,blank=True)

    def __str__(self):
        return self.image_name
    
    # def get_image_url(self):
    #     # Assuming your images are served statically, modify this method accordingly
    #     return f"/get_files/{self.id}.jpeg"

    # def get_crop_image_url(self):
    #     # Assuming your cropped images are served statically, modify this method accordingly
    #     return f"/home/pooja/WAD/{self.cropped_image_name}"

class Video(models.Model):
    title = models.CharField(max_length=100,null=True,blank=True)
    link = models.CharField(max_length=200,null=True,blank=True)
    hd_quality = models.BooleanField(default=False,null=True,blank=True)
    own_rights = models.BooleanField(default=False,null=True,blank=True)
    grant_permission = models.BooleanField(default=False,null=True,blank=True)
    reason = models.CharField(max_length=200, null=True, blank=True)

    # Define a foreign key relationship with Person
    person = models.ForeignKey('Person', on_delete=models.CASCADE, related_name='video_person',null=True,blank=True)

    def __str__(self):
        return self.title


class Podcast(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    link = models.CharField(max_length=255, null=True, blank=True)
    source = models.CharField(max_length=255, null=True, blank=True)

    # Define a foreign key relationship with Person
    person = models.ForeignKey('Person', on_delete=models.CASCADE, related_name='podcasts_person', null=True, blank=True)

    def __str__(self):
        return self.title


class Book(models.Model):
    upload_book_image = models.FileField(upload_to='get_files/', null=True, blank=True)
    book_name = models.CharField(max_length=255, null=True, blank=True)
    title = models.CharField(max_length=255, null=True, blank=True)
    description = models.CharField(max_length=1000, null=True, blank=True)
    authors = models.CharField(max_length=255, null=True, blank=True)
    publisher = models.CharField(max_length=255, null=True, blank=True)
    link = models.CharField(max_length=255, null=True, blank=True)
    cost_per_book_cad = models.CharField(max_length=255, null=True, blank=True)
    bulk_order_purchase_offered = models.BooleanField( null=True, blank=True)
    price_per_book_cad = models.CharField(max_length=255, null=True, blank=True)
    number_of_books = models.IntegerField( null=True, blank=True)

    # Define a foreign key relationship with Person
    person = models.ForeignKey('Person', on_delete=models.CASCADE, related_name='person_book', null=True, blank=True)

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
    person = models.ForeignKey('Person', on_delete=models.CASCADE, related_name='white_papers_case_studies_persons',null=True,blank=True)

    def __str__(self):
        return self.title

class DegreesCertificatesAwards(models.Model):
    degree_data = models.FileField(upload_to='get_files/', null=True, blank=True)
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
    person = models.ForeignKey('Person', on_delete=models.CASCADE, related_name='speaker_contact_information_person',null=True,blank=True)

class ManagerOrTeammate(models.Model):
    assist_coordinating = models.BooleanField()
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    pronouns = models.CharField(max_length=50)
    cell_phone = models.CharField(max_length=20)
    main_email = models.CharField(max_length=100)
    website = models.CharField(max_length=200)
    person = models.ForeignKey('Person', on_delete=models.CASCADE, related_name='manager_or_teammate_person',null=True,blank=True)

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
    person = models.ForeignKey('Person', on_delete=models.CASCADE, related_name='social_media_personal_person',null=True,blank=True)


class BusinessInfo(models.Model):
    issue_payment = models.BooleanField()
    official_business_name = models.CharField(max_length=100)
    business_email = models.CharField(max_length=100)
    business_phone = models.CharField(max_length=15)
    business_number = models.CharField(max_length=20)
    website = models.CharField(max_length=200)
    person = models.ForeignKey('Person', on_delete=models.CASCADE, related_name='person_business_info',null=True,blank=True)

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
    person = models.ForeignKey('Person', on_delete=models.CASCADE, related_name='social_media_business_person',null=True,blank=True)

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
    using_presentation_software = models.BooleanField(null=True,blank=True)
    presentation_software_name = models.CharField(max_length=255,null=True,blank=True)
    using_audience_interaction_software = models.BooleanField(null=True,blank=True)
    audience_interaction_software_name = models.CharField(max_length=255,null=True,blank=True)
    attending_sessions_before_after_presentation = models.BooleanField(null=True,blank=True)
    attending_meals_networking_sessions = models.BooleanField(null=True,blank=True)
    dietary_requirements_restrictions = models.CharField(max_length=255,null=True,blank=True)
    A_V_requirements = models.CharField(max_length=255,null=True,blank=True)
    prefer_to_book_travel = models.CharField(max_length=255,null=True,blank=True)
    prefer_to_book_travel = models.BooleanField(null=True,blank=True)
    use_travel_agent = models.BooleanField(null=True,blank=True)
    Preferred_Seating = models.CharField(max_length=255,null=True,blank=True)
    Preferred_Airline = models.CharField(max_length=255,null=True,blank=True)
    West_Jet_number = models.CharField(max_length=255,null=True,blank=True)
    Air_Canada_number = models.CharField(max_length=255)
    special_conditions_for_travel_arrangements = models.BooleanField(null=True,blank=True)
    table_for_book_sales = models.BooleanField(null=True,blank=True)
    person = models.ForeignKey('Person', on_delete=models.CASCADE,null=True,blank=True)

class SpeakerIntroduction(models.Model):
    introduction_text = models.CharField(max_length=255,null=True,blank=True)
    at_events = models.ForeignKey(AtEvents, on_delete=models.CASCADE, related_name='speaker_introduction',null=True,blank=True)

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
    person = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='help_us_book_you_person',null=True,blank=True)


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
    person = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='help_us_work_with_you_person',null=True,blank=True)


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
    person = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='person_fee',null=True,blank=True)

    class Meta:
        verbose_name_plural = 'Fees'

class SpeakerPitch(models.Model):
    general_pitch = models.CharField(max_length=255)
    keyword_topic_focus_pitch = models.CharField(max_length=255)
    Short_pitch_up = models.CharField(max_length=255)
    person = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='speaker_pitches_person',null=True,blank=True)

    class Meta:
        verbose_name_plural = 'SpeakerPitches'

class PreviousClient(models.Model):
    organization_name = models.CharField(max_length=255)
    person = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='previous_clients_person',null=True,blank=True)

    class Meta:
        verbose_name_plural = 'PreviousClients'