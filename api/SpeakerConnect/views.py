import io
import json
import random
import string
import uuid
from django.conf import settings
from django.http import FileResponse
from django.shortcuts import get_object_or_404
import requests
from rest_framework import viewsets
import os
from .serializers import *
from rest_framework.response import Response
from PIL import Image
from io import BytesIO
import base64
from rest_framework import status
from rest_framework.decorators import api_view
from datetime import datetime


class SpeakerTopicViewSet(viewsets.ModelViewSet):
    queryset = SpeakerTopic.objects.all()
    serializer_class = SpeakerTopicSerializer

class BiographyViewSet(viewsets.ModelViewSet):
    queryset = Biography.objects.all()
    serializer_class = BiographySerializer

class TopicDescriptionViewSet(viewsets.ModelViewSet):
    queryset = TopicDescription.objects.all()
    serializer_class = TopicDescriptionSerializer

class TestimonialViewSet(viewsets.ModelViewSet):
    queryset = Testimonial.objects.all()
    serializer_class = TestimonialSerializer

class ImagesViewSet(viewsets.ModelViewSet):
    queryset = Images.objects.all()
    serializer_class = ImagesSerializer

class VideoViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer

class PodcastViewSet(viewsets.ModelViewSet):
    queryset = Podcast.objects.all()
    serializer_class = PodcastSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class MediaMentionViewSet(viewsets.ModelViewSet):
    queryset = MediaMention.objects.all()
    serializer_class = MediaMentionSerializer

class WhitePaperCaseStudyViewSet(viewsets.ModelViewSet):
    queryset = WhitePaperCaseStudy.objects.all()
    serializer_class = WhitePaperCaseStudySerializer

class DegreesCertificatesAwardsViewSet(viewsets.ModelViewSet):
    queryset = DegreesCertificatesAwards.objects.all()
    serializer_class = DegreesCertificatesAwardsSerializer



class SpeakerContactInformationViewSet(viewsets.ModelViewSet):
    queryset = SpeakerContactInformation.objects.all()
    serializer_class = SpeakerContactInformationSerializer

    def create(self, request, person_id=None):
        person_id = person_id or self.kwargs.get('person_id')  
        request.data['person'] = person_id

        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)

class ManagerOrTeammateViewSet(viewsets.ModelViewSet):
    queryset = ManagerOrTeammate.objects.all()
    serializer_class = ManagerOrTeammateSerializer

class SocialMediaPersonalViewSet(viewsets.ModelViewSet):
    queryset = SocialMediaPersonal.objects.all()
    serializer_class = SocialMediaPersonalSerializer

class BusinessInfoViewSet(viewsets.ModelViewSet):
    queryset = BusinessInfo.objects.all()
    serializer_class = BusinessInfoSerializer

class SocialMediaBusinessViewSet(viewsets.ModelViewSet):
    queryset = SocialMediaBusiness.objects.all()
    serializer_class = SocialMediaBusinessSerializer

class BrandCampaignOrganizationtheme1ViewSet(viewsets.ModelViewSet):
    queryset = BrandCampaignOrganizationtheme1.objects.all()
    serializer_class = BrandCampaignOrganizationtheme1Serializer

class BrandCampaignOrganizationtheme2ViewSet(viewsets.ModelViewSet):
    queryset = BrandCampaignOrganizationtheme2.objects.all()
    serializer_class = BrandCampaignOrganizationtheme2Serializer

class AtEventsViewSet(viewsets.ModelViewSet):
    queryset = AtEvents.objects.all()
    serializer_class = AtEventsSerializer

class SpeakerIntroductionViewSet(viewsets.ModelViewSet):
    queryset = SpeakerIntroduction.objects.all()
    serializer_class = SpeakerIntroductionSerializer

class HelpUsBookYouViewSet(viewsets.ModelViewSet):
    queryset = HelpUsBookYou.objects.all()
    serializer_class = HelpUsBookYouSerializer

class HelpUsWorkWithYouViewSet(viewsets.ModelViewSet):
    queryset = HelpUsWorkWithYou.objects.all()
    serializer_class = HelpUsWorkWithYouSerializer

class FeesViewSet(viewsets.ModelViewSet):
    queryset = Fees.objects.all()
    serializer_class = FeesSerializer

class SpeakerPitchViewSet(viewsets.ModelViewSet):
    queryset = SpeakerPitch.objects.all()
    serializer_class = SpeakerPitchSerializer

class PreviousClientViewSet(viewsets.ModelViewSet):
    queryset = PreviousClient.objects.all()
    serializer_class = PreviousClientSerializer

class SpeakerTagViewSet(viewsets.ModelViewSet):
    queryset = SpeakerTag.objects.all()
    serializer_class = SpeakerTagSerializer

class DescriptiveTitlesViewSet(viewsets.ModelViewSet):
    queryset = DescriptiveTitles.objects.all()
    serializer_class = DescriptiveTitlesSerializer
    
@api_view(['POST'])
def create_person(request):
    serializer = PersonSerializer(data=request.data)
    if serializer.is_valid():
        otp = ''.join(random.choices(string.digits, k=6))
        person = serializer.save(otp=otp, otp_verified=False)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def login(request):
    username = request.data.get('username')
    password = request.data.get('password')

    try:
        person = Person.objects.get(username=username)
    except Person.DoesNotExist:
        return Response("Invalid username or password", status=status.HTTP_401_UNAUTHORIZED)

    if person.otp_verified:
        if check_password(password,person.password):
            return Response({"message": "Login successful!", "id": person.id}, status=status.HTTP_200_OK)
        else:
            return Response("Invalid username or password", status=status.HTTP_401_UNAUTHORIZED)
    else:
        return Response("OTP verification required", status=status.HTTP_401_UNAUTHORIZED)



@api_view(['POST'])
def verify_otp(request):
    username = request.data.get('username')
    otp_entered = request.data.get('otp')

    try:
        person = Person.objects.get(username=username)
    except Person.DoesNotExist:
        return Response("Invalid username", status=status.HTTP_401_UNAUTHORIZED)

    if person.otp == otp_entered:
        # OTP verification successful
        person.otp_verified = True
        person.save()
        return Response({"message": "OTP verified"}, status=status.HTTP_200_OK)
    else:
        return Response("Invalid OTP", status=status.HTTP_401_UNAUTHORIZED)




@api_view(['POST'])
def create_speaker_contact_info(request, person_id):
    try:
        data = request.data

        # Extract data for SpeakerContactInformation
        speaker_contact_info_data = data.get('speaker_contact_information')
        speaker_contact_info = SpeakerContactInformation.objects.create(
            first_name=speaker_contact_info_data['first_name'],
            last_name=speaker_contact_info_data['last_name'],
            middle_initials=speaker_contact_info_data.get('middle_initials'),
            secondary_names_nick_name=speaker_contact_info_data.get('secondary_names_nick_name'),
            pronouns=speaker_contact_info_data['pronouns'],
            cell_phone=speaker_contact_info_data['cell_phone'],
            main_email=speaker_contact_info_data['main_email'],
            website_link=speaker_contact_info_data['website_link'],
            rss_blog_link=speaker_contact_info_data['rss_blog_link'],
            rss_blog_link_2=speaker_contact_info_data['rss_blog_link_2'],
            closest_major_airport=speaker_contact_info_data['closest_major_airport']
        )

        # Extract data for ManagerOrTeammate
        manager_teammate_data = data.get('manager_or_teammate')
        manager_teammate_contact_info = manager_teammate_data.get('contact_info')
        manager_teammate = ManagerOrTeammate.objects.create(
            assist_coordinating=manager_teammate_data['assist_coordinating'],
            first_name=manager_teammate_contact_info['first_name'],
            last_name=manager_teammate_contact_info['last_name'],
            pronouns=manager_teammate_contact_info['pronouns'],
            cell_phone=manager_teammate_contact_info['cell_phone'],
            main_email=manager_teammate_contact_info['main_email'],
            website=manager_teammate_contact_info['website']
        )
        # Extract data for SocialMediaPersonal
        social_media_personal_data = data.get('social_media_personal')
        social_media_personal = SocialMediaPersonal.objects.create(
            facebook_link=social_media_personal_data['facebook']['link'],
            facebook_handle=social_media_personal_data['facebook']['handle'],
            facebook_followers=social_media_personal_data['facebook']['followers'],
            instagram_link=social_media_personal_data['instagram']['link'],
            instagram_handle=social_media_personal_data['instagram']['handle'],
            instagram_followers=social_media_personal_data['instagram']['followers'],
            twitter_link=social_media_personal_data['twitter']['link'],
            twitter_handle=social_media_personal_data['twitter']['handle'],
            twitter_followers=social_media_personal_data['twitter']['followers'],
            linkedin_link=social_media_personal_data['linkedin']['link'],
            linkedin_handle=social_media_personal_data['linkedin']['handle'],
            linkedin_followers=social_media_personal_data['linkedin']['followers'],
            tiktok_link=social_media_personal_data['tiktok']['link'],
            tiktok_handle=social_media_personal_data['tiktok']['handle'],
            tiktok_followers=social_media_personal_data['tiktok']['followers']
        )


        person = Person.objects.get(pk=person_id)
        if person is None:
            return Response({'error': 'Person not found with the specified person_id'}, status=404)

        speaker_contact_info.person = person
        speaker_contact_info.save()

        manager_teammate.person = person
        manager_teammate.save()

        social_media_personal.person = person
        social_media_personal.save()
        

        return Response({'message': 'Speaker contact information created successfully'}, status=201)
    except Exception as e:
        return Response({'error': str(e)}, status=400)
    

# ------------------------------------- Create biography ----------------------------------------------------------

speaker_topic_enum_dict = {
    'Accessibility': 'accessibility',
    'Adaptability & Agility': 'adaptability_amp_agility',
    'Addictions & Substance Abuse': 'addictions_amp_substance_abuse',
    'Alliances & Partnerships': 'alliances_amp_partnerships',
    'Artificial Intelligence (AI)': 'artificial_intelligenceAI',
    'Big Data': 'bigdata',
    'Blockchain & Metaverse': 'blockchain_amp_metaverse',
    'Bullying At Work': 'bullyingatwork',
    'Burnout Prevention': 'burnoutprevention',
    'Business & Corporate': 'business_amp_corporate',
    'Business Ethics & Values': 'business_ethics_amp_values',
    'Business Growth': 'businessgrowth',
    'Business Leadership': 'business_leadership',
    'Business Management': 'business_management',
    'Business Technology': 'business_technology',
    'Business Transitions': 'business_transitions',
    'Change Management': 'change_management',
    'Collaboration': 'collaboration',
    'Communications': 'communications',
    'Conflict Resolution': 'conflict_resolution',
    'Consumer Behaviour & Retail': 'consumer_behaviour_amp_retail',
    'Corporate Responsibility (CSR)': 'corporate_responsibility_CSR',
    'Cultural Diversity': 'cultural_diversity',
    'Customer Service': 'customer_service',
    'Cyber Security': 'cyber_security',
    'Digital Marketing': 'digital_marketing',
    'Disability': 'disability',
    'Disruption Management': 'disruption_management',
    'Disruptive Innovation': 'disruptive_innovation',
    'Diversity & Inclusion': 'Diversity_amp_inclusion',
    'Economics': 'economics',
    'Emotional Intelligence': 'emotional_intelligence',
    'Employee Engagement': 'employee_engagement',
    'Employee Management': 'employee_management',
    'Employee Retention': 'employee_retention',
    'Entrepreneurship': 'entrepreneurship',
    'Excellence & Success': 'Excellence_amp_success',
    'Future of Work': 'future_of_work',
    'Future Trends': 'future_trends',
    'Futurists': 'futurists',
    'Gender Equality': 'gender_equality',
    'Generations At Work': 'generations_at_work',
    'Generational Differences': 'genrational_differences',
    'Global Business Solutions': 'global_business_solutions',
    'Happiness & Positivity': 'happiness_amp_positivity',
    'Health & Human Performance': 'health_amp_human_performance',
    'Health & Wellness': 'health_amp_wellness',
    'HR & Corporate Culture': 'hr_amp_corporate_culture',
    'Humour At Workplace': 'humour_at_workplace',
    'Inclusive Leadership': 'inclusive_leadership',
    'Indigenous': 'indigenous',
    'Influence & Negotiation': 'influence_amp_negotiation',
    'Innovation & Creativity': 'innovation_amp_creativity',
    'Inter-Generational Workplace': 'inter_generational_workplace',
    'Leadership': 'leadership',
    'Leadership & Change': 'leadership_amp_change',
    'Leadership Development': 'leadership_development',
    'LGBTQ2S+': 'LGBTQ2S+',
    'Marketing & Branding': 'marketing_amp_branding',
    'Memory Networking': 'memory_networking',
    'Mental Health': 'mental_health',
    'Mentoring At Work': 'mentoring_at_work',
    'Mergers & Acquisitions': 'mergers_amp_acquisitions',
    'Mindfulness': 'mindfulness',
    'Mindset & Attitude': 'mindset_amp_attitude',
    'Mindset & Goal Accomplishment': 'mindset_amp_goal_accomplishment',
    'Neurodiversity': 'neurodiversity',
    'Nutrition & Fitness': 'nutrition_amp_fitness',
    'Organizational Change': 'organizational_change',
    'Organizational Leadership': 'organizational_leadership',
    'Peak Performance': 'peak_performance',
    'Personal Growth': 'personal_growth',
    'Personal Leadership': 'personal_leadership',
    'Positive Psychology': 'positive_psychology',
    'Presentation Skills': 'presentation_skills',
    'Privacy': 'privacy',
    'Process & Systems': 'process_amp_systems',
    'Project Management': 'project_management',
    'Psychological Safety': 'psychological_safety',
    'PTSD & Trauma': 'ptsd_amp_trauma',
    'Public Relations': 'public_relations',
    'Purposeful Work': 'purposeful_work',
    'Racial Justice': 'racial_justice',
    'Resilience & Adversity': 'resilience_amp_adversity',
    'Resilience & Change': 'resilience_amp_change',
    'Sales': 'sales',
    'Self Improvement & Self Care': 'self_improvement_amp_self_care',
    'Small Business Development': 'small_business_development',
    'Social Media': 'social_media',
    'Soft Skills Development': 'soft_skills_development',
    'STEM': 'stem',
    'Strategic Thinking': 'strategic_thinking',
    'Stress Management': 'stress_management',
    'Suicide Prevention': 'suicide_prevention',
    'Talent Management': 'talent_management',
    'Teamwork': 'teamwork',
    'Tech Trends': 'tech_trends',
    'Time Management': 'time_management',
    'Transformation': 'transformation',
    'Trust & Relationships': 'trust_relationships',
    'Unconscious Bias': 'unconscious_bias',
    'Women In Business': 'women_in_business',
    'Women Of Influence': 'women_of_influence',
    "Women's Leadership": 'womens_leadership',
    "Women's Rights & MeToo": 'womens_rights_amp_metoo',
    'Work Life Balance': 'work_life_balance',
    'Workplace Culture': 'workplace_culture'
}


speaker_tags_enum_dict = {
    'ReactJs': 'reactjs',
    'Html': 'html',
    'Java': 'java',
    'Python': 'python',
}

descriptive_titles_enum_dict = {
    'Academia': 'academia',
    'Adventurers': 'adventurers',
    'Agriculture & Farming': 'agriculture & farming',
    'All Staff Meeting': 'all staff meeting',
    'Annual General Meetings': 'annual general meetings',
    'Associations & Unions': 'associations & unions',
    'Athletes & Sports': 'athletes & sports',
    'Award Galas & After Dinner': 'award galas & after dinner',
    'Awareness Days': 'awareness days',
    'Bilingual & French': 'bilingual & french',
    'Board Meetings & Strategic Advisory': 'board meetings & strategic advisory',
    'Campus & University Speakers': 'campus & university speakers',
    'Cancer Awareness': 'cancer awareness',
    'Career Development': 'career development',
    'Celebrity': 'celebrity',
    'Certified Speakers': 'certified speakers',
    'Certified Speaking Professionals CSP': 'certified speaking professionals csp',
    'Charities & Foundations': 'charities & foundations',
    'Community Engagement Events': 'community engagement events',
    'Conference': 'conference',
    'Conferences & Summits': 'conferences & summits',
    'Consultant & Coach': 'consultant & coach',
    'Corporate Audience': 'corporate audience',
    'Corporate Entertainers': 'corporate entertainers',
    'Corporations & Businesses': 'corporations & businesses',
    'Department Meeting': 'department meeting',
    'Economic Development': 'economic development',
    'Education & Teachers': 'education & teachers',
    'Endorsement & Product Launch': 'endorsement & product launch',
    'Environment & Climate Change': 'environment & climate change',
    'Event Hosts & Moderators': 'event hosts & moderators',
    'Executive Leadership & C-Suite': 'executive leadership & c-suite',
    'Family & Parenting': 'family & parenting',
    'Finance & Insurance': 'finance & insurance',
    'First Nation Motivational Speakers': 'first nation motivational speakers',
    'First Responders': 'first responders',
    'Fundraisers & Banquets': 'fundraisers & banquets',
    'Funny & Comedy': 'funny & comedy',
    'Government Departments & Agencies': 'government departments & agencies',
    'Guest Panelist & Guided Q&A': 'guest panelist & guided q&a',
    'Hall of Fame': 'hall of fame',
    'Health and Safety': 'health and safety',
    'Healthcare': 'healthcare',
    'Home & Garden': 'home & garden',
    'Hybrid Workplace': 'hybrid workplace',
    'Industry Types': 'industry types',
    'Infrastructure & Urban Planning': 'infrastructure & urban planning',
    'Inspirational': 'inspirational',
    'Interactive & Experience': 'interactive & experience',
    'Key Note': 'key note',
    'Lifestyle & Health': 'lifestyle & health',
    'Managing Remote Employees': 'managing remote employees',
    'Medical & Healthcare': 'medical & healthcare',
    'Men': 'men',
    'Mentalists & Hypnotists': 'mentalists & hypnotists',
    'Military': 'military',
    'Most Requested': 'most requested',
    'Motivation': 'motivation',
    'Mountain Climbers': 'mountain climbers',
    'Non Binary': 'non binary',
    'Olympians & Olympics': 'olympians & olympics',
    'Opening & Closing Keynote': 'opening & closing keynote',
    'Orateur & Conférencier': 'orateur & conférencier',
    'Patient Safety & Patient Care': 'patient safety & patient care',
    'Philanthropy & Giving Back': 'philanthropy & giving back',
    'Professional Development Days PD Days': 'professional development days pd days',
    'Politicians': 'politicians',
    'Presentation Formats': 'presentation formats',
    'Real Estate': 'real estate',
    'Research & Science': 'research & science',
    'Safety': 'safety',
    'Sales Motivation & Sales Kick Off': 'sales motivation & sales kick off',
    'School Boards': 'school boards',
    'Scientific & Technical': 'scientific & technical',
    'Social & Cultural': 'social & cultural',
    'Social Justice & Human Rights': 'social justice & human rights',
    'Sort By': 'sort by',
    'Speaker Types': 'speaker types',
    'Staff Appreciation & Employee Recognition': 'staff appreciation & employee recognition',
    'Storytelling': 'storytelling',
    'Sustainable Development': 'sustainable development',
    'TED & TEDx': 'ted & tedx',
    'Town Halls & Retreats': 'town halls & retreats',
    'Trade Shows & Conventions': 'trade shows & conventions',
    'Under $5,000': 'under $5,000',
    'Virtual & Online Meetings': 'virtual & online meetings',
    'Virtual Engagement': 'virtual engagement',
    'Virtual Speakers': 'virtual speakers',
    'Virtual Teams & Remote Workers': 'virtual teams & remote workers',
    'Women': 'women',
    'Workshop & Training': 'workshop & training',
    'Youth Leadership & Students': 'youth leadership & students',
    'Youth Leadership and Student Empowerment': 'youth leadership and student empowerment',
}


@api_view(['POST'])
def create_biography(request, person_id):
    try:
        # Extracting data from the request
        microphone_files = request.FILES.getlist('Microphone')
        microphonetext = request.data.get('Microphonetext')
        highlight = request.data.get('Highlight')
        sort_bio = request.data.get('Sort_Bio')
        long_bio = request.data.get('Long_Bio')
        speaker_topics_additional_keywords = request.data.get('Additional_keywords')
        descriptive_title_type = request.data.get('Descriptive_title_type')
        speaker_topics = request.data.getlist('speaker_topics')
        speaker_tags = request.data.getlist('speaker_tags')
        descriptive_titles = request.data.getlist('descriptive_titles')
        city = request.data.get('City')
        province_state = request.data.get('Province_State')

        person = Person.objects.get(pk=person_id)


        new_bio = Biography.objects.create(
            highlight=highlight,
            microphonetext=microphonetext,
            sort_bio=sort_bio,
            long_bio=long_bio,
            speaker_topics_additional_keywords=speaker_topics_additional_keywords,
            descriptive_title_type=descriptive_title_type,
            city=city,
            province_state=province_state,
            person=person
        )

        for topic in speaker_topics:
            if speaker_topic_enum_dict.get(topic):
                new_bio.speaker_topics.add(SpeakerTopic.objects.create(topic=topic))

        for tag in speaker_tags:
            validated_tag = speaker_tags_enum_dict.get(tag)
            if validated_tag:  
                new_bio.speaker_tags.add(SpeakerTag.objects.create(tag=validated_tag))

        for title in descriptive_titles:
            if descriptive_titles_enum_dict.get(title):  
                new_bio.descriptive_titles.add(DescriptiveTitles.objects.create(title=title))

        for file in microphone_files:
            new_bio.microphone.save(file.name, file, save=True)
            new_bio.microphone_name = file.name

        return Response({'message': 'Biography created successfully'}, status=201)

    except Exception as e:
        return Response({'error': str(e)}, status=500)
    

# ------------------------------------------------------- Topic descriptions -----------------------------------------------



@api_view(['POST'])
def create_topicdescription(request, person_id):
    try:
        topic_description_data = request.data.get('topic_description_data', [])
        person = Person.objects.get(pk=person_id)

        created_topic_descriptions = []

        if topic_description_data:
            topic_data_list = json.loads(topic_description_data)

            for topic_data in topic_data_list:
                new_topic_description = TopicDescription.objects.create(
                    title=topic_data.get('Topic_Description_Title', ''),
                    body_text=topic_data.get('Topic_Description_Body_Text', ''),
                    delivered_as=topic_data.get('Topic_delivered_as', ''),
                    audiotext=topic_data.get('Audio_text', ''),
                    video_clip=topic_data.get('Video_Clip_for_Topic_Description_1', ''),
                    person = person
                )

                audio_clip_data = topic_data.get('Audio_Clip_for_Topic_Description_1', '')
                new_topic_description.audio_clip = audio_clip_data

                # person.topic_descriptions.add(new_topic_description)
                created_topic_descriptions.append({
                    'topic_id': new_topic_description.id,
                    'title': new_topic_description.title,
                    'body_text': new_topic_description.body_text,
                    'delivered_as': new_topic_description.delivered_as,
                    'audiotext': new_topic_description.audiotext,
                    'video_clip': new_topic_description.video_clip,
                    'audio_clip': new_topic_description.audio_clip
                })

            return Response({'message': 'Topic descriptions created successfully', 'created_topic_descriptions': created_topic_descriptions}, status=status.HTTP_201_CREATED)

        return Response({'message': 'No topic description data provided'}, status=status.HTTP_400_BAD_REQUEST)

    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



# ----------------------------------- Image ---------------------------------------------------------------------------


@api_view(['POST'])
def create_image(request, person_id):
    try:
        data_str = request.data.get('image_data')
        data = json.loads(data_str)
        person = Person.objects.get(pk=person_id)

        created_images = []

        for image_data in data:
            image_binary = base64.b64decode(image_data.get('src', ''))
            crop_image_binary = base64.b64decode(image_data.get('original_image', ''))

            try:
                img = Image.open(io.BytesIO(image_binary))
                img.verify()

                image_extension = img.format.lower()

                new_image = Images(
                    own_right=image_data.get('own_rights', ''),
                    sbc_permission=image_data.get('sbc_permissions', ''),
                    person=person
                )

                if image_binary and image_extension:
                    image_name = f"{str(uuid.uuid4())}.{image_extension}"
                    new_image.image_name = f'{image_name}'

                    media_root = settings.MEDIA_ROOT
                    image_path = os.path.join(media_root, 'get_files', image_name)
                    os.makedirs(os.path.dirname(image_path), exist_ok=True)

                    with open(image_path, 'wb') as image_file:
                        image_file.write(image_binary)

                if crop_image_binary:
                    crop_img = Image.open(io.BytesIO(crop_image_binary))
                    crop_img.verify()

                    cropped_image_name = f"{str(uuid.uuid4())}.{image_extension}"
                    new_image.cropped_image_name = f'{cropped_image_name}'

                    crop_image_path = os.path.join(media_root, 'get_files', cropped_image_name)
                    os.makedirs(os.path.dirname(crop_image_path), exist_ok=True)

                    with open(crop_image_path, 'wb') as crop_image_file:
                        crop_image_file.write(crop_image_binary)

                new_image.save()  

                created_images.append({
                    'image_id': new_image.id,
                    'own_rights': new_image.own_right,
                    'sbc_permissions': new_image.sbc_permission,
                    'image_url': f'{settings.MEDIA_URL}get_files/{new_image.image_name}',
                    'src': f'{settings.MEDIA_URL}get_files/{new_image.cropped_image_name}' if new_image.cropped_image_name else None,
                    'image_name': new_image.image_name if image_binary else None,
                    'cropped_image_name': new_image.cropped_image_name if crop_image_binary else None,
                })
            except Exception as e:
                return Response({'error': f'Invalid image data: {e}'}, status=status.HTTP_400_BAD_REQUEST)

        return Response({'message': 'Images created successfully', 'created_images': created_images}, status=status.HTTP_201_CREATED)

    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    


#--------------------------------------- VIDEO -----------------------------------------------------------------------

@api_view(['POST'])
def create_videos(request, person_id):
    try:
        data = request.data.get('Video')
        
        person = get_object_or_404(Person, pk=person_id)
        
        for video_data in data:
            title = video_data.get('Title')
            link = video_data.get('Link')
            source_info = video_data.get('source_if_not', {})
            hd_quality = source_info.get('HD_Quality')
            own_rights = source_info.get('Do_you_own_the_rights_to_this_video')
            grant_permission = source_info.get('Do_you_grant_SBC_permission_and_all_clients_permission_to_use_this_video_for_promoting_you_as_a_speaker')
            reason = video_data.get('why_not')

            video = Video.objects.create(
                title=title,
                link=link,
                hd_quality=hd_quality,
                own_rights=own_rights,
                grant_permission=grant_permission,
                reason=reason,
                person=person  
            )

        return Response({'message': 'Videos created successfully'}, status=201)
    except Exception as e:
        return Response({'error': str(e)}, status=400)



# ---------------------------------------- Poadcast-------------------------------------------------------------------------

@api_view(['POST'])
def create_podcasts(request, person_id):
    try:
        podcasts_data = request.data.get('podcasts')

        person = Person.objects.get(pk=person_id)
        if not person:
            return Response({'error': 'Person not found with the specified person_id'}, status=404)

        for podcast_info in podcasts_data:
            serializer = PodcastSerializer(data=podcast_info)
            if serializer.is_valid():
                serializer.save(person=person)
            else:
                return Response(serializer.errors, status=400)

        return Response({'message': 'Podcasts created successfully'}, status=201)
    except Exception as e:
        return Response({'error': str(e)}, status=400)



# ------------------------------------- Create Books --------------------------------------------------------------------



@api_view(['POST'])
def create_books(request, person_id):
    data_str = request.data.get('books_data')
    data = json.loads(data_str)

    try:
        person = Person.objects.get(pk=person_id)
    except Person.DoesNotExist:
        return Response({'error': 'Person not found'}, status=404)

    created_books = []

    for book_data in data:
        book_data_binary = base64.b64decode(book_data.get('book_file', ''))

        book_image_extension = None
        with BytesIO(book_data_binary) as book_image_stream:
            book = Image.open(book_image_stream)
            book_image_extension = book.format.lower()

        new_book = Book(

            title=book_data.get('book_title', ''),
            description=book_data.get('book_description', ''),
            authors=book_data.get('book_authors', ''),
            publisher=book_data.get('book_publisher', ''),
            link=book_data.get('book_link', ''),
            cost_per_book_cad=book_data.get('book_cost', ''),
            bulk_order_purchase_offered=str(book_data.get('book_bulkorder', '')).lower() == 'true',
            price_per_book_cad=book_data.get('book_price', ''),
            number_of_books=book_data.get('book_number', ''),
            person=person 
        )

        media_root = settings.MEDIA_ROOT
        media_url = settings.MEDIA_URL


        if book_data_binary:
            book_image_extension = book_image_extension or 'jpg' 
            new_book.book_name = f"{str(uuid.uuid4())}.{book_image_extension}" 
            image_dir = os.path.join(media_root, 'get_files')
            os.makedirs(image_dir, exist_ok=True)

            book_path = os.path.join(image_dir, new_book.book_name)
            with open(book_path, 'wb') as book_file:
                book_file.write(book_data_binary)

            new_book.save()
            # person.books.add(new_book)

        created_books.append({
            'upload_book_image_url':  f'{settings.MEDIA_URL}get_files/{new_book.book_name}',
            'book_id': new_book.id,
            'title': new_book.title,
            'description': new_book.description,
            'authors': new_book.authors,
            'publisher': new_book.publisher,
            'link': new_book.link,
            'cost_per_book_cad': new_book.cost_per_book_cad,
            'bulk_order_purchase_offered': new_book.bulk_order_purchase_offered,
            'price_per_book_cad': new_book.price_per_book_cad,
            'number_of_books': new_book.number_of_books
        })

    response_data = {'message': 'Books created successfully', 'created_books': created_books}
    return Response(response_data, status=201)


# --------------------------------- Create Media -------------------------------------------------------------------


@api_view(['POST'])
def create_media_mentions(request, person_id):
    try:
        data = request.data

        media_mentions_data = data.get('media_mentions')

        person = Person.objects.get(pk=person_id)
        if person is None:
            return Response({'error': 'Person not found with the specified person_id'}, status=404)

        for media_data in media_mentions_data:
            organization_name = media_data.get('organization_name')
            interview_article_titles = media_data.get('interview_article_title')
            link = media_data.get('link')
            date = media_data.get('date')
            interview_source_name = media_data.get('interview_source_name')

            interview_article_title = ', '.join(interview_article_titles)

            media_mention = MediaMention.objects.create(
                organization_name=organization_name,
                interview_article_title=interview_article_title,
                link=link,
                date=datetime.strptime(date, '%Y-%m-%d').date(),  
                interview_source_name=interview_source_name,
                person=person
            )

        return Response({'message': 'Media mentions created successfully'}, status=201)
    except Exception as e:
        return Response({'error': str(e)}, status=400)




# ---------------------------------------------- White papers/case ------------------------------------------------------------


@api_view(['POST'])
def create_white_papers_case_studies(request, person_id):
    try:
        data = request.data

        white_papers_data = data.get('white_papers_case_studies')

        person = Person.objects.get(pk=person_id)
        if person is None:
            return Response({'error': 'Person not found with the specified person_id'}, status=404)

        for white_paper_data in white_papers_data:
            organization_name = white_paper_data.get('organization_name')
            title = white_paper_data.get('title')
            topics = white_paper_data.get('topics')
            description = white_paper_data.get('description')
            link = white_paper_data.get('link')
            date = white_paper_data.get('date')

            white_paper = WhitePaperCaseStudy.objects.create(
                organization_name=organization_name,
                title=title,
                topics=topics,
                description=description,
                link=link,
                date=date,
                person = person
            )
            # person.white_papers_case_studies.add(white_paper)

        return Response({'message': 'White papers/case studies created successfully'}, status=201)
    except Exception as e:
        return Response({'error': str(e)}, status=400)



# -------------------------------------- DegreesCertificatesAwards -------------------------------------------------------------

@api_view(['POST'])
def create_degrees_certifications_awards(request, person_id):
    try:
        person = Person.objects.get(pk=person_id)
        if person is None:
            return Response({'error': 'Person not found with the specified person_id'}, status=404)
        
        degreescertificatesawards = request.FILES.getlist('degreescertificatesawards')
        
        for file in degreescertificatesawards:
            if file:
                new_degrees = DegreesCertificatesAwards.objects.create(
                    person=person,
                    degree_data=file, 
                    degreescertificatesawards_name=file.name
                )
                
        return Response({'message': 'degrees_certifications_awards files created successfully'}, status=201)
    
    except Exception as e:
        return Response({'error': str(e)}, status=500)




# --------------------------------------------- Testimonial ---------------------------------------------------------------

@api_view(['POST'])
def create_testimonial(request, person_id):
    try:
        person = get_object_or_404(Person, pk=person_id)
        
        data = request.data
        testimonials_data = data.get('Testimonials', [])

        for testimonial_data in testimonials_data:
            organizer_name = testimonial_data.get('Organizer_Name')
            organization_name = testimonial_data.get('Testimonial_Organization_Name')
            link_to_video = testimonial_data.get('Link_to_Video')

            testimonial = Testimonial.objects.create(
                organizer_name=organizer_name,
                organization_name=organization_name,
                link_to_video=link_to_video,
                person=person
            )

        return Response({'message': 'Testimonials created successfully'}, status=201)
    except Exception as e:
        return Response({'error': str(e)}, status=400)




# ------------------------------------------- BusinessInfo ---------------------------------------------------------------

@api_view(['POST'])
def create_business_info(request, person_id):
    try:
        person = get_object_or_404(Person, pk=person_id)
        
        data = request.data

        business_info_data = data.get('business_info')
        social_media_business_data = data.get('social_media_business')

        business_info = BusinessInfo.objects.create(
            issue_payment=business_info_data['business_issue_payment'],
            official_business_name=business_info_data['business_information']['official_business_name'],
            business_email=business_info_data['business_information']['business_email'],
            business_phone=business_info_data['business_information']['business_phone'],
            business_number=business_info_data['business_information']['business_number'],
            website=business_info_data['business_information']['website'],
            person=person
        )
        # person.business_info = business_info

        social_media_business = SocialMediaBusiness.objects.create(
            facebook_link=social_media_business_data['facebook']['link'],
            facebook_handle=social_media_business_data['facebook']['handle'],
            facebook_followers=social_media_business_data['facebook']['followers'],
            instagram_link=social_media_business_data['instagram']['link'],
            instagram_handle=social_media_business_data['instagram']['handle'],
            instagram_followers=social_media_business_data['instagram']['followers'],
            twitter_link=social_media_business_data['twitter']['link'],
            twitter_handle=social_media_business_data['twitter']['handle'],
            twitter_followers=social_media_business_data['twitter']['followers'],
            linkedin_link=social_media_business_data['linkedin']['link'],
            linkedin_handle=social_media_business_data['linkedin']['handle'],
            linkedin_followers=social_media_business_data['linkedin']['followers'],
            tiktok_link=social_media_business_data['tiktok']['link'],
            tiktok_handle=social_media_business_data['tiktok']['handle'],
            tiktok_followers=social_media_business_data['tiktok']['followers'],
            person=person
        )
        # person.social_media_business = social_media_business
        
        # person.save()

        return Response({'message': 'Business information created successfully'}, status=201)
    except Exception as e:
        return Response({'error': str(e)}, status=400)



# ------------------------------------------------ BrandCampaignOrganizationTheme1 ------------------------------------------

@api_view(['POST'])
def create_brand_campaigns(request, person_id):
    try:
        person = get_object_or_404(Person, pk=person_id)

        data = request.data

        brand_campaigns_data1 = data.get('Brand_Product_CampaignsEndorsementstheme1')
        brand_campaigns_data2 = data.get('Brand_Product_CampaignsEndorsementstheme2')

        for organization_data in brand_campaigns_data1:
            part_of_social_media = organization_data.get('part_of_social_media', False)
            organization_name = organization_data.get('organization_name')
            platforms = organization_data.get('platforms')
            link_to_campaign = organization_data.get('link_to_campaign')
            start_year = organization_data.get('start_year')
            end_year = organization_data.get('end_year')

            brand_campaign = BrandCampaignOrganizationtheme1.objects.create(
                part_of_social_media=part_of_social_media,
                organization_name=organization_name,
                platforms=platforms,
                link_to_campaign=link_to_campaign,
                start_year=start_year,
                end_year=end_year,
                person=person
            )

        for organization_data in brand_campaigns_data2:
            part_of_social_media = organization_data.get('part_of_social_media', False)
            organization_name = organization_data.get('organization_name')
            platforms = organization_data.get('platforms')
            link_to_campaign = organization_data.get('link_to_campaign')
            start_year = organization_data.get('start_year')
            end_year = organization_data.get('end_year')

            brand_campaign = BrandCampaignOrganizationtheme2.objects.create(
                part_of_social_media=part_of_social_media,
                organization_name=organization_name,
                platforms=platforms,
                link_to_campaign=link_to_campaign,
                start_year=start_year,
                end_year=end_year,
                person=person
            )

        return Response({'message': 'Brand/Product Campaigns & Endorsements created successfully'}, status=201)
    except Exception as e:
        return Response({'error': str(e)}, status=400)



# ------------------------------------------- At Events ------------------------------------------------------------------


@api_view(['POST'])
def create_at_events(request, person_id):
    try:
        person = get_object_or_404(Person, pk=person_id)

        data = request.data
        at_events_data = data.get('at_events')[0] 

        at_events = AtEvents.objects.create(
            using_presentation_software=at_events_data['presentation_software']['using_presentation_software'],
            presentation_software_name=at_events_data['presentation_software']['presentation_software_name'],
            using_audience_interaction_software=at_events_data['audience_interaction_software']['using_audience_interaction_software'],
            audience_interaction_software_name=at_events_data['audience_interaction_software']['audience_interaction_software_name'],
            attending_sessions_before_after_presentation=at_events_data['attending_sessions_before_after_presentation'],
            attending_meals_networking_sessions=at_events_data['meal_networking_session']['attending_meals_networking_sessions'],
            dietary_requirements_restrictions=at_events_data['meal_networking_session']['dietary_requirements_restrictions'],
            A_V_requirements=at_events_data['meal_networking_session']['A_V_requirements'],
            prefer_to_book_travel=at_events_data['prefer_to_book_travel'],
            special_conditions_for_travel_arrangements=at_events_data['special_conditions_for_travel_arrangements'],
            table_for_book_sales=at_events_data['table_for_book_sales'],
            person = person
        )

        speaker_introductions_data = at_events_data['meal_networking_session']['speaker_introduction']
        for introduction_data in speaker_introductions_data:
            for key, introduction_text in introduction_data.items():
                speaker_introduction = SpeakerIntroduction.objects.create(
                    introduction_text=introduction_text
                )
                at_events.speaker_introduction.add(speaker_introduction)

        travel_agent_data = at_events_data.get('travel_agent', {})
        use_travel_agent = travel_agent_data.get('use_travel_agent', False)
        Preferred_Seating = travel_agent_data.get('Preferred_Seating', '')
        Preferred_Airline = travel_agent_data.get('Preferred_Airline', '')
        West_Jet_number = travel_agent_data.get('West_Jet#', '')
        Air_Canada_number = travel_agent_data.get('Air_Canada#', '')

        at_events.use_travel_agent = use_travel_agent
        at_events.Preferred_Seating = Preferred_Seating
        at_events.Preferred_Airline = Preferred_Airline
        at_events.West_Jet_number = West_Jet_number
        at_events.Air_Canada_number = Air_Canada_number

        # person.at_events = at_events
        # person.save()

        return Response({'message': 'At Events and Speaker Introduction created successfully'}, status=201)
    except Exception as e:
        return Response({'error': str(e)}, status=400)





# ----------------------------------------------- Help Us Book You -----------------------------------------------------------


@api_view(['POST'])
def create_help_us_book_you(request, person_id):
    try:
        person = get_object_or_404(Person, pk=person_id)

        data = request.data
        help_us_book_you_data = data.get('Help_us_book_you')

        help_us_book_you = HelpUsBookYou.objects.create(
            speaker_reason_to_work_with=help_us_book_you_data['speaker_reason_to_work_with'],
            value_adds_and_offerings=help_us_book_you_data['value_adds_and_offerings']['offer_any_value_adds'],
            books_how_many_items=help_us_book_you_data['value_adds_and_offerings']['books']['how_many_items'],
            books_value_per_item=help_us_book_you_data['value_adds_and_offerings']['books']['value_per_item'],
            online_training_how_many_items=help_us_book_you_data['value_adds_and_offerings']['online_training']['how_many_items'],
            online_training_value_per_item=help_us_book_you_data['value_adds_and_offerings']['online_training']['value_per_item'],
            merch_how_many_items=help_us_book_you_data['value_adds_and_offerings']['merch']['how_many_items'],
            merch_value_per_item=help_us_book_you_data['value_adds_and_offerings']['merch']['value_per_item'],
            merch_2_how_many_items=help_us_book_you_data['value_adds_and_offerings']['merch_2']['how_many_items'],
            merch_2_value_per_item=help_us_book_you_data['value_adds_and_offerings']['merch_2']['value_per_item'],
            complementary_virtual_follow_sessions_consultation=help_us_book_you_data['complementary_virtual_follow_sessions_consultation'],
            inclusive_of_travel_expenses=help_us_book_you_data['inclusive_of_travel_expenses'],
            industries_do_you_not_work_with=help_us_book_you_data['industry_you_specialize_with']['industries_do_you_not_work_with'],
            favorite_audiences_event_types=help_us_book_you_data['industry_you_specialize_with']['favorite_audiences_event_types'],
            target_audiences_industries=help_us_book_you_data['industry_you_specialize_with']['target_audiences_industries'],
            English_French=help_us_book_you_data['English_&_French'],
            Q_A_in_French=help_us_book_you_data['Q&A_in_French'],
            offer_recordings=help_us_book_you_data['offer_recordings'],
            primary_source_of_income=help_us_book_you_data['primary_source_of_income'],
            hoping_for_speaking_to_become_your_primary_source_income=help_us_book_you_data['speaking_frequency']['hoping_for_speaking_to_become_your_primary_source_income'],
            current_speak_per_month=help_us_book_you_data['speaking_frequency']['current_speak_per_month'],
            virtual_events_over_pandemic=help_us_book_you_data['speaking_frequency']['virtual_events_over_pandemic'],
            speak_per_month=help_us_book_you_data['speaking_frequency']['speak_per_month'],
            market_yourself_as_a_speaker=help_us_book_you_data['speaking_frequency']['market_yourself_as_a_speaker'],
            affiliated_with_any_other_speakers_agencies=help_us_book_you_data['speaking_frequency']['affiliated_with_any_other_speakers_agencies'],
            percentage_of_bookings=help_us_book_you_data['speaking_frequency']['percentage_of_bookings'],
            Approximately_what_percentage=help_us_book_you_data['speaking_frequency']['Approximately_what_percentage'],
            speakers_are_you_affiliated_with=help_us_book_you_data['speaking_frequency']['speakers_are_you_affiliated_with'],
            person = person
        )

        # person.help_us_book_you = help_us_book_you
        # person.save()

        return Response({'message': 'Help Us Book You created successfully'}, status=201)
    except Exception as e:
        return Response({'error': str(e)}, status=400)


# ------------------------------------------------ Help Us Work With You --------------------------------------------------

@api_view(['POST'])
def create_help_us_work_with_you(request, person_id):
    try:
        person = get_object_or_404(Person, pk=person_id)

        data = request.data
        help_us_work_with_you_data = data.get('Help_us_work_with_you')

        help_us_work_with_you = HelpUsWorkWithYou.objects.create(
            newsletter_onboarding=help_us_work_with_you_data['newsletter_onboarding'],
            tracking_system=help_us_work_with_you_data['tracking_system'],
            whatsapp=help_us_work_with_you_data['whatsapp'],
            business_ownership=help_us_work_with_you_data['business_ownership'],
            crm_usage=help_us_work_with_you_data['crm_usage'],
            appointment_booking_software=help_us_work_with_you_data['appointment_booking_software'],
            expectations_with_sbc=help_us_work_with_you_data['expectations_with_sbc'],
            something_about_you=help_us_work_with_you_data['something_about_you'],
            stories=help_us_work_with_you_data['stories'],
            person = person
        )

        # person.help_us_work_with_you = help_us_work_with_you
        # person.save()

        return Response({'message': 'Help Us Work With You created successfully'}, status=201)
    except Exception as e:
        return Response({'error': str(e)}, status=400)


#------------------------------------------- Fees --------------------------------------------------------------------

@api_view(['POST'])
def create_fees(request, person_id):
    try:
        person = get_object_or_404(Person, pk=person_id)

        fees_data = request.data.get('Fees')

        fees = Fees.objects.create(
            Pro_Bono_Events=fees_data['Pro_Bono_Events'],
            Corporate_Keynote_20_60_Minutes=fees_data['Discounted_Rate_Events']['Corporate_Keynote_20-60_Minutes'],
            Corporate_Workshop_60_120_Minutes=fees_data['Discounted_Rate_Events']['Corporate_Workshop_60-120_Minutes'],
            Corporate_Half_Day_Training_or_Keynote_Breakout=fees_data['Discounted_Rate_Events']['Corporate_Half_Day_Training_or_Keynote_Breakout'],
            Corporate_Full_Day_Training=fees_data['Discounted_Rate_Events']['Corporate_Full_Day_Training'],
            Concurrent_Sessions_Fee=fees_data['Multiple_Sessions_on_the_Same_Day']['Concurrent_Sessions_Fee'],
            One_Session_in_the_Morning_Fee=fees_data['Multiple_Sessions_on_the_Same_Day']['One_Session_in_the_Morning_Fee'],
            One_Session_in_the_Afternoon_Fee=fees_data['Multiple_Sessions_on_the_Same_Day']['One_Session_in_the_Afternoon_Fee'],
            Multiple_Sessions_on_Concurrent_Days=fees_data['Multiple_Sessions_on_Concurrent_Days'],
            Multiple_Sessions_Over_a_Period_of_Time=fees_data['Multiple_Sessions_Over_a_Period_of_Time'],
            Lowest_Acceptance_for_Informal_Talk=fees_data['Lowest_Acceptance_for_Informal_Talk'],
            One_Day_Event=fees_data['Host_or_Emcee_Fees']['One_Day_Event'],
            One_Day_Plus_Evening_Ceremony_Keynote=fees_data['Host_or_Emcee_Fees']['One_Day_Plus_Evening_Ceremony_Keynote'],
            Two_Day_Event=fees_data['Host_or_Emcee_Fees']['Two_Day_Event'],
            Two_Day_Plus_Evening_Ceremony_Keynote=fees_data['Host_or_Emcee_Fees']['Two_Day_Plus_Evening_Ceremony_Keynote'],
            Three_Day_Event=fees_data['Host_or_Emcee_Fees']['Three_Day_Event'],
            Three_Day_Plus_Evening_Ceremony_Keynote=fees_data['Host_or_Emcee_Fees']['Three_Day_Plus_Evening_Ceremony_Keynote'],
            Four_Day_Event=fees_data['Host_or_Emcee_Fees']['Four_Day_Event'],
            Four_Day_Plus_Evening_Ceremony_Keynote=fees_data['Host_or_Emcee_Fees']['Four_Day_Plus_Evening_Ceremony_Keynote'],
            What_is_your_corporate_speaker_fee=fees_data['Host_or_Emcee_Fees']['What_is_your_corporate_speaker_fee'],
            lowest_you_will_accept=fees_data['Host_or_Emcee_Fees']['lowest_you_will_accept'],
            limitations_or_condition=fees_data['Host_or_Emcee_Fees']['limitations_or_condition'],
            Driving_Distance_Fee=fees_data['Host_or_Emcee_Fees']['Driving_Distance_Fee'],
            Province_Fee=fees_data['Host_or_Emcee_Fees']['Province_Fee'],
            Western_Canada_Fee=fees_data['Host_or_Emcee_Fees']['Western_Canada_Fee'],
            Eastern_Canada_Fee=fees_data['Host_or_Emcee_Fees']['Eastern_Canada_Fee'],
            Northern_Canada_Fee=fees_data['Host_or_Emcee_Fees']['Northern_Canada_Fee'],
            Remote_Location_Fee=fees_data['Host_or_Emcee_Fees']['Remote_Location_Fee'],
            Local_Discount=fees_data['Local_Discount']['Local_Discount'],
            Local_Fee=fees_data['Local_Discount']['Local_Fee'],
            Client_Direct_Approach_for_Local_Event=fees_data['Local_Discount']['Client_Direct_Approach_for_Local_Event'],
            Virtual_Discount=fees_data['Virtual_Discount']['Virtual_Discountt'],
            Virtual_Fee=fees_data['Virtual_Discount']['Virtual_Fee'],
            Client_Direct_Approach_for_Virtual_Event=fees_data['Virtual_Discount']['Client_Direct_Approach_for_Virtual_Event'],
            Small_Audience_Discount=fees_data['Small_Audience_Discount']['Small_Audience_Discountt'],
            Small_Audience_Fee=fees_data['Small_Audience_Discount']['Small_Audience_Fee'],
            Client_Direct_Approach_for_Small_Audience_Event=fees_data['Small_Audience_Discount']['Client_Direct_Approach_for_Small_Audience_Event'],
            Qualification_for_Small_Audience=fees_data['Small_Audience_Discount']['Qualification_for_Small_Audience'],
            Nonprofit_Discount=fees_data['Nonprofit_Discount']['Nonprofit_Discountt'],
            Nonprofit_Fee=fees_data['Nonprofit_Discount']['Nonprofit_Fee'],
            Client_Direct_Approach_for_Nonprofit=fees_data['Nonprofit_Discount']['Client_Direct_Approach_for_Nonprofit'],
            Charitable_Organization_Discount=fees_data['Charitable_Organization_Discount']['Charitable_Organization_Discountt'],
            Charitable_Fee=fees_data['Charitable_Organization_Discount']['Charitable_Fee'],
            Client_Direct_Approach_for_Charitable_Organization=fees_data['Charitable_Organization_Discount']['Client_Direct_Approach_for_Charitable_Organization'],
            outside_of_speaker_fee_ranges=fees_data['Charitable_Organization_Discount']['outside_of_speaker_fee_ranges'],
            Rate_Increase=fees_data['Rate_Increase'],
            person = person
        )

        # person.fees = fees
        # person.save()

        return Response({'message': 'Fees created successfully'}, status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)





# ------------------------------------------------ Speaker pitches --------------------------------------------------------

@api_view(['POST'])
def create_speaker_pitches(request, person_id):
    try:
        person = get_object_or_404(Person, pk=person_id)

        speaker_pitches_data = request.data.get('speaker_pitches')

        for pitch_data in speaker_pitches_data:
            speaker_pitch = SpeakerPitch.objects.create(
                general_pitch=pitch_data['general_pitch'],
                keyword_topic_focus_pitch=pitch_data['keyword_topic_focus_pitch'],
                Short_pitch_up=pitch_data['Short_pitch_up'],
                person = person
            )
            # person.speaker_pitches.add(speaker_pitch)

        return Response({'message': 'Speaker pitches created successfully'}, status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)




# ----------------------------------- Previous clients -------------------------------------------------------------------

@api_view(['POST'])
def create_previous_clients(request, person_id):
    try:
        person = get_object_or_404(Person, pk=person_id)

        previous_clients_data = request.data.get('previous_clients', [])

        previous_clients = []

        for client_data in previous_clients_data:
            if isinstance(client_data, dict):
                organization_name = client_data.get('organization_name')
                client = PreviousClient.objects.create(organization_name=organization_name,person = person)
                previous_clients.append(client)
            else:
                organization_name = client_data
                client = PreviousClient.objects.create(organization_name=organization_name,person = person)
                previous_clients.append(client)

        # person.previous_clients.clear()
        # person.previous_clients.add(*previous_clients)

        return Response({'message': 'Previous clients created successfully'}, status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


# ---------------------------------------- Upload Files ---------------------------------------------------------------


@api_view(['GET'])
def get_files(request, filename):
    file_path = os.path.join(settings.MEDIA_ROOT, filename)

    if os.path.exists(file_path):
        with open(file_path, 'rb') as file:
            response = FileResponse(file)
            return response

    return Response('File not found', status=404)



#------------------------------------------Get All Data-----------------------------------------------------------------------

@api_view(['GET'])
def get_all_data(request, person_id):
    try:
        person = Person.objects.get(pk=person_id)
        if person is None:
            return Response({'error': 'Person not found with the specified person_id'}, status=404)
        
        serializer = PersonSerializer(person)
        serialized_data = serializer.data

        # Extract data for Biography

        biographies = []
        biographies_data = Biography.objects.filter(person=person)
        for biography in biographies_data:
            biographies_data = {
                'biography_id': biography.id,
                'highlight': biography.highlight,
                'long_bio': biography.long_bio,
                'sort_bio': biography.sort_bio,
                'speaker_topics_additional_keywords': biography.speaker_topics_additional_keywords,
                'descriptive_title_type': biography.descriptive_title_type,
                'city': biography.city,
                'province_state': biography.province_state,
                'microphone_url' : f'{settings.MEDIA_URL}{biography.microphone.name}' if biography.microphone else None,
                'speaker_topics': [topic.topic for topic in biography.speaker_topics.all()],
                'descriptive_titles': [title.title for title in biography.descriptive_titles.all()],
                'speaker_tags': [tag.tag for tag in biography.speaker_tags.all()]
            }
            biographies.append(biographies_data)

        # Extract data for manager_or_teammate
        manager_or_teammate = []
        manager_teammates = ManagerOrTeammate.objects.filter(person=person)
        for manager_teammate in manager_teammates:
            manager_data = {
                'assist_coordinating': manager_teammate.assist_coordinating,
                'contact_info': {
                    'id': manager_teammate.id,
                    'first_name': manager_teammate.first_name,
                    'last_name': manager_teammate.last_name,
                    'pronouns': manager_teammate.pronouns,
                    'cell_phone': manager_teammate.cell_phone,
                    'main_email': manager_teammate.main_email,
                    'website': manager_teammate.website,
                }
            }
            manager_or_teammate.append(manager_data)


        # Extract data for speaker_contact_information
        speaker_contact_infos = SpeakerContactInformation.objects.filter(person=person)

        speaker_contact_info_data = []
        for info in speaker_contact_infos:
            speaker_contact_info_data.append({
                'id': info.id,
                'first_name': info.first_name,
                'last_name': info.last_name,
                'middle_initials': info.middle_initials,
                'secondary_names_nick_name': info.secondary_names_nick_name,
                'pronouns': info.pronouns,
                'cell_phone': info.cell_phone,
                'main_email': info.main_email,
                'website_link': info.website_link,
                'rss_blog_link': info.rss_blog_link,
                'rss_blog_link_2': info.rss_blog_link_2,
                'closest_major_airport': info.closest_major_airport,
            })

        # Extract data for SocialMediaPersonal
        social_media_personal_list = []
        social_media_personal_data = SocialMediaPersonal.objects.filter(person=person)
        for social_media in social_media_personal_data:
            social_media_info = {
                'facebook': {
                    'link': social_media.facebook_link,
                    'handle': social_media.facebook_handle,
                    'followers': social_media.facebook_followers,
                },
                'instagram': {
                    'link': social_media.instagram_link,
                    'handle': social_media.instagram_handle,
                    'followers': social_media.instagram_followers,
                },
                'twitter': {
                    'link': social_media.twitter_link,
                    'handle': social_media.twitter_handle,
                    'followers': social_media.twitter_followers,
                },
                'linkedin': {
                    'link': social_media.linkedin_link,
                    'handle': social_media.linkedin_handle,
                    'followers': social_media.linkedin_followers,
                },
                'tiktok': {
                    'link': social_media.tiktok_link,
                    'handle': social_media.tiktok_handle,
                    'followers': social_media.tiktok_followers,
                }
            }
            social_media_personal_list.append(social_media_info)

        # Extract data for Fees

        fees = []
        fees_data = Fees.objects.filter(person=person)
        for fee in fees_data:
            fee_data = {
                'id': fee.id,
                'Pro_Bono_Events': fee.Pro_Bono_Events,
                'Corporate_Keynote_20_60_Minutes': fee.Corporate_Keynote_20_60_Minutes,
                'Corporate_Workshop_60_120_Minutes': fee.Corporate_Workshop_60_120_Minutes,
                'Corporate_Half_Day_Training_or_Keynote_Breakout': fee.Corporate_Half_Day_Training_or_Keynote_Breakout,
                'Corporate_Full_Day_Training': fee.Corporate_Full_Day_Training,
                'Concurrent_Sessions_Fee': fee.Concurrent_Sessions_Fee,
                'One_Session_in_the_Morning_Fee': fee.One_Session_in_the_Morning_Fee,
                'One_Session_in_the_Afternoon_Fee': fee.One_Session_in_the_Afternoon_Fee,
                'Multiple_Sessions_on_Concurrent_Days': fee.Multiple_Sessions_on_Concurrent_Days,
                'Multiple_Sessions_Over_a_Period_of_Time': fee.Multiple_Sessions_Over_a_Period_of_Time,
                'Lowest_Acceptance_for_Informal_Talk': fee.Lowest_Acceptance_for_Informal_Talk,
                'One_Day_Event': fee.One_Day_Event,
                'One_Day_Plus_Evening_Ceremony_Keynote': fee.One_Day_Plus_Evening_Ceremony_Keynote,
                'Two_Day_Event': fee.Two_Day_Event,
                'Two_Day_Plus_Evening_Ceremony_Keynote': fee.Two_Day_Plus_Evening_Ceremony_Keynote,
                'Three_Day_Event': fee.Three_Day_Event,
                'Three_Day_Plus_Evening_Ceremony_Keynote': fee.Three_Day_Plus_Evening_Ceremony_Keynote,
                'Four_Day_Event': fee.Four_Day_Event,
                'Four_Day_Plus_Evening_Ceremony_Keynote': fee.Four_Day_Plus_Evening_Ceremony_Keynote,
                'What_is_your_corporate_speaker_fee': fee.What_is_your_corporate_speaker_fee,
                'lowest_you_will_accept': fee.lowest_you_will_accept,
                'limitations_or_condition': fee.limitations_or_condition,
                'Driving_Distance_Fee': fee.Driving_Distance_Fee,
                'Province_Fee': fee.Province_Fee,
                'Western_Canada_Fee': fee.Western_Canada_Fee,
                'Eastern_Canada_Fee': fee.Eastern_Canada_Fee,
                'Northern_Canada_Fee': fee.Northern_Canada_Fee,
                'Remote_Location_Fee': fee.Remote_Location_Fee,
                'Local_Discount': fee.Local_Discount,
                'Local_Fee': fee.Local_Fee,
                'Client_Direct_Approach_for_Local_Event': fee.Client_Direct_Approach_for_Local_Event,
                'Virtual_Discount': fee.Virtual_Discount,
                'Virtual_Fee': fee.Virtual_Fee,
                'Client_Direct_Approach_for_Virtual_Event': fee.Client_Direct_Approach_for_Virtual_Event,
                'Small_Audience_Discount': fee.Small_Audience_Discount,
                'Small_Audience_Fee': fee.Small_Audience_Fee,
                'Client_Direct_Approach_for_Small_Audience_Event': fee.Client_Direct_Approach_for_Small_Audience_Event,
                'Qualification_for_Small_Audience': fee.Qualification_for_Small_Audience,
                'Nonprofit_Discount': fee.Nonprofit_Discount,
                'Nonprofit_Fee': fee.Nonprofit_Fee,
                'Client_Direct_Approach_for_Nonprofit': fee.Client_Direct_Approach_for_Nonprofit,
                'Charitable_Organization_Discount': fee.Charitable_Organization_Discount,
                'Charitable_Fee': fee.Charitable_Fee,
                'Client_Direct_Approach_for_Charitable_Organization': fee.Client_Direct_Approach_for_Charitable_Organization,
                'outside_of_speaker_fee_ranges': fee.outside_of_speaker_fee_ranges,
                'Rate_Increase': fee.Rate_Increase,
            }
            fees.append(fee_data)


         # Extract data for Images
        images_data = Images.objects.filter(person_id=person_id)

        images = []

        for image in images_data:
            image_info = {
                'image_id': image.id,
                'image_name': image.image_name,
                'crop_image_name': image.cropped_image_name,
                'image_url' : f'{settings.MEDIA_URL}get_files/{image.image_name}',
                'src': f'{settings.MEDIA_URL}get_files/{image.cropped_image_name}' if image.cropped_image_name else None,
            }

            images.append(image_info)



        # Extract data for Books
        books_data = Book.objects.filter(person_id=person_id)

        all_books_data = []

        for book in books_data:
            book_info = {
                'id': book.id,
                'title': book.title,
                'description': book.description,
                'authors': book.authors,
                'publisher': book.publisher,
                'link': book.link,
                'cost_per_book_cad': book.cost_per_book_cad,
                'bulk_order_purchase_offered': book.bulk_order_purchase_offered,
                'price_per_book_cad': book.price_per_book_cad,
                'number_of_books': book.number_of_books,
                'upload_book_image_url': f'{settings.MEDIA_URL}get_files/{book.book_name}',
            }

            all_books_data.append(book_info)


        # Extract data for DegreesCertificatesAwards
        degrees_data = DegreesCertificatesAwards.objects.filter(person_id=person_id)
        all_degrees_data = []

        for degree in degrees_data:
            degree_url = None

            if degree.degree_data:
                file_name = str(degree.degree_data).split('/')[-1] 
                degree_url = f'{settings.MEDIA_URL}get_files/{file_name}'  

            degree_info = {
                'degree_id': degree.id,
                'degree_data_url': degree_url,
            }

            all_degrees_data.append(degree_info)


        # Extract data for topic_descriptions
        topic_descriptions = []

        topic_des = TopicDescription.objects.filter(person_id=person_id)

        for topic_description in topic_des:
            topic_data = {
                'id': topic_description.id,
                'audiotext': topic_description.audiotext,
                'title': topic_description.title,
                'body_text': topic_description.body_text,
                'delivered_as': topic_description.delivered_as,
                'video_link': topic_description.video_clip,
                'audio_clip': topic_description.audio_clip
            }

            topic_descriptions.append(topic_data)



         # Extract data for BrandCampaignOrganizationtheme1
        brand_campaigns_data1 = []

        bp_camp = BrandCampaignOrganizationtheme1.objects.filter(person_id=person_id)

        for brand_campaign in  bp_camp:
            brand_campaign = {'id': brand_campaign.id,
            'part_of_social_media': brand_campaign.part_of_social_media,
            'organization_name': brand_campaign.organization_name,
            'platforms': brand_campaign.platforms,
            'link_to_campaign': brand_campaign.link_to_campaign,
            'start_year': brand_campaign.start_year,
            'end_year': brand_campaign.end_year}
            

            brand_campaigns_data1.append(brand_campaign)


         # Extract data for BrandCampaignOrganizationtheme2

        brand_campaigns_data2 = []

        bp_camp2 = BrandCampaignOrganizationtheme2.objects.filter(person_id=person_id)

        for brand_campaign in  bp_camp2:
            brand_campaign = {'id': brand_campaign.id,
            'part_of_social_media': brand_campaign.part_of_social_media,
            'organization_name': brand_campaign.organization_name,
            'platforms': brand_campaign.platforms,
            'link_to_campaign': brand_campaign.link_to_campaign,
            'start_year': brand_campaign.start_year,
            'end_year': brand_campaign.end_year}
            

            brand_campaigns_data2.append(brand_campaign)


         # Extract data for HelpUsBookYou

        help_us_book_you_data1 = []
        help_us_book_you = HelpUsBookYou.objects.filter(person_id=person_id)
        for data in help_us_book_you:
            help_us_book_you_data = {
                'id': data.id,
                'speaker_reason_to_work_with': data.speaker_reason_to_work_with,
                'value_adds_and_offerings': {
                    'offer_any_value_adds': data.value_adds_and_offerings,
                    'books': {
                        'how_many_items': data.books_how_many_items,
                        'value_per_item': data.books_value_per_item
                    },
                    'online_training': {
                        'how_many_items': data.online_training_how_many_items,
                        'value_per_item': data.online_training_value_per_item
                    },
                    'merch': {
                        'how_many_items': data.merch_how_many_items,
                        'value_per_item':data.merch_value_per_item
                    },
                    'merch_2': {
                        'how_many_items': data.merch_2_how_many_items,
                        'value_per_item': data.merch_2_value_per_item
                    },
                },
                'complementary_virtual_follow_sessions_consultation': data.complementary_virtual_follow_sessions_consultation,
                'inclusive_of_travel_expenses': data.inclusive_of_travel_expenses,
                'industry_you_specialize_with': {
                    'industries_do_you_not_work_with': data.industries_do_you_not_work_with,
                    'favorite_audiences_event_types': data.favorite_audiences_event_types,
                    'target_audiences_industries': data.target_audiences_industries,
                },
                'English_&_French': data.English_French,
                'Q&A_in_French': data.Q_A_in_French,
                'offer_recordings': data.offer_recordings,
                'primary_source_of_income': data.primary_source_of_income,
                'speaking_frequency': {
                    'hoping_for_speaking_to_become_your_primary_source_income':data.hoping_for_speaking_to_become_your_primary_source_income,
                    'current_speak_per_month': data.current_speak_per_month,
                    'virtual_events_over_pandemic': data.virtual_events_over_pandemic,
                    'speak_per_month': data.speak_per_month,
                    'market_yourself_as_a_speaker': data.market_yourself_as_a_speaker,
                    'affiliated_with_any_other_speakers_agencies':data.affiliated_with_any_other_speakers_agencies,
                    'percentage_of_bookings': data.percentage_of_bookings,
                    'Approximately_what_percentage': data.Approximately_what_percentage,
                    'speakers_are_you_affiliated_with':data.speakers_are_you_affiliated_with
                }
            }

            help_us_book_you_data1.append(help_us_book_you_data)


        # Extract data for Help Us Work With You
        help_us_work_with_you_data = []
        help_us_work_with_you = HelpUsWorkWithYou.objects.filter(person_id=person_id)
        for data in help_us_work_with_you:
            help_us_to_work = {
                'id': data.id,
                'newsletter_onboarding': data.newsletter_onboarding,
                'tracking_system': data.tracking_system,
                'whatsapp': data.whatsapp,
                'business_ownership': data.business_ownership,
                'crm_usage': data.crm_usage,
                'appointment_booking_software': data.appointment_booking_software,
                'expectations_with_sbc': data.expectations_with_sbc,
                'something_about_you': data.something_about_you,
                'stories': data.stories,
            }

            help_us_work_with_you_data.append(help_us_to_work)


        # Extract data for AtEvents
        at_events_data = []
        event_data = AtEvents.objects.filter(person_id=person_id)
        for data in event_data:
            at_events_data1 = {
                'id': data.id,
                'presentation_software': {
                    'using_presentation_software': data.using_presentation_software,
                    'presentation_software_name': data.presentation_software_name
                },
                'audience_interaction_software': {
                    'using_audience_interaction_software': data.using_audience_interaction_software,
                    'audience_interaction_software_name': data.audience_interaction_software_name
                },
                'attending_sessions_before_after_presentation':data.attending_sessions_before_after_presentation,
                'meal_networking_session': {
                    'attending_meals_networking_sessions': data.attending_meals_networking_sessions,
                    'dietary_requirements_restrictions': data.dietary_requirements_restrictions,
                    'A_V_requirements': data.A_V_requirements,
                    'speaker_introduction': []
                },
                'prefer_to_book_travel': data.prefer_to_book_travel,
                'special_conditions_for_travel_arrangements': data.special_conditions_for_travel_arrangements,
                'table_for_book_sales': data.table_for_book_sales,
                'travel_agent': {
                    'use_travel_agent': data.use_travel_agent,
                    'Preferred_Seating': data.Preferred_Seating,
                    'Preferred_Airline': data.Preferred_Airline,
                    'West_Jet#': data.West_Jet_number,
                    'Air_Canada#': data.Air_Canada_number
                }
            }

            for introduction in data.speaker_introduction.all():
                at_events_data['meal_networking_session']['speaker_introduction'].append({
                    'id': introduction.id,
                    'introduction_text': introduction.introduction_text
                })

            at_events_data.append(at_events_data1)


        # Extract data for business information
        business_info_data = []
        business_info = BusinessInfo.objects.filter(person_id=person_id)
        for data in business_info:
            business_info_data1 = {
                'id': data.id,
                'business_issue_payment': data.issue_payment,
                'business_information': {
                    'official_business_name': data.official_business_name,
                    'business_email': data.business_email,
                    'business_phone': data.business_phone,
                    'business_number': data.business_number,
                    'website': data.website,
                }
            }
            business_info_data.append(business_info_data1)

        # Extract data for media mentions
        media_mentions_data = []
        media_mentions = MediaMention.objects.filter(person_id=person_id)
        for media_mention in media_mentions:
            interview_article_titles = media_mention.interview_article_title.split(', ')
            media_mentions_data.append({
                'id': media_mention.id,
                'organization_name': media_mention.organization_name,
                'interview_article_title': interview_article_titles,
                'link': media_mention.link,
                'date': media_mention.date,
                'interview_source_name': media_mention.interview_source_name
            })

        # Extract data for podcasts
        podcast_data = []
        podcasts = Podcast.objects.filter(person_id=person_id)
        for podcast in podcasts:
            podcast_data.append({
                'id': podcast.id,
                'title': podcast.title,
                'link': podcast.link,
                'source': podcast.source
            })

        # Extract data for Previous Clients
        previous_clients_data = []
        previous_clients = PreviousClient.objects.filter(person_id=person_id)
        for client in previous_clients:
            client_data = {
                'id': client.id,  # Include the ID
                'organization_name': client.organization_name,
                
            }
            previous_clients_data.append(client_data)


         # Extract data for Speaker Pitches
        speaker_pitches_data = []
        speaker_pitches = SpeakerPitch.objects.filter(person_id=person_id)
        for pitch in speaker_pitches:
            pitch_data = {
                'id': pitch.id,
                'general_pitch': pitch.general_pitch,
                'keyword_topic_focus_pitch': pitch.keyword_topic_focus_pitch,
                'Short_pitch_up': pitch.Short_pitch_up,

            }
            speaker_pitches_data.append(pitch_data)


        # Extract data for social media (business)
        social_media_business_data = []
        social_media_business = SocialMediaBusiness.objects.filter(person_id=person_id)
        for data in social_media_business:
            social_media_business_data1 = {
                'id': data.id,
                'facebook': {
                    'link': data.facebook_link,
                    'handle': data.facebook_handle,
                    'followers': data.facebook_followers
                },
                'instagram': {
                    'link': data.instagram_link,
                    'handle': data.instagram_handle,
                    'followers': data.instagram_followers
                },
                'twitter': {
                    'link': data.twitter_link,
                    'handle': data.twitter_handle,
                    'followers': data.twitter_followers
                },
                'linkedin': {
                    'link': data.linkedin_link,
                    'handle': data.linkedin_handle,
                    'followers': data.linkedin_followers
                },
                'tiktok': {
                    'link': data.tiktok_link,
                    'handle': data.tiktok_handle,
                    'followers': data.tiktok_followers
                }
            }

            social_media_business_data.append(social_media_business_data1)


         # Extract data for social_media_personal
        social_media_personal_data = []
        social_media_personal1 = SocialMediaPersonal.objects.filter(person_id=person_id)
        for social_media_personal in social_media_personal1:
            social_media_personal2 = {
                'id': social_media_personal.id,
                'facebook': {
                    'link': social_media_personal.facebook_link,
                    'handle': social_media_personal.facebook_handle,
                    'followers': social_media_personal.facebook_followers,
                },
                'instagram': {
                    'link': social_media_personal.instagram_link,
                    'handle': social_media_personal.instagram_handle,
                    'followers': social_media_personal.instagram_followers,
                },
                'twitter': {
                    'link': social_media_personal.twitter_link,
                    'handle': social_media_personal.twitter_handle,
                    'followers': social_media_personal.twitter_followers,
                },
                'linkedin': {
                    'link': social_media_personal.linkedin_link,
                    'handle': social_media_personal.linkedin_handle,
                    'followers': social_media_personal.linkedin_followers,
                },
                'tiktok': {
                    'link': social_media_personal.tiktok_link,
                    'handle': social_media_personal.tiktok_handle,
                    'followers': social_media_personal.tiktok_followers,
                },
            }
            social_media_personal_data.append(social_media_personal2)
            

        # Extract data for white papers and case studies
        white_papers_case_studies_data = []
        white_papers_case_studies = WhitePaperCaseStudy.objects.filter(person_id=person_id)
        for white_paper in white_papers_case_studies:
            white_papers_case_studies_data.append({
                'id': white_paper.id,
                'organization_name': white_paper.organization_name,
                'title': white_paper.title,
                'topics': white_paper.topics,
                'description': white_paper.description,
                'link': white_paper.link,
                'date': white_paper.date
            })

        
        # Extract data for testimonials
        testimonials_data = []
        testimonials = Testimonial.objects.filter(person_id=person_id)
        for testimonial in testimonials:
            testimonials_data.append({
                'id': testimonial.id,
                'Organizer_Name': testimonial.organizer_name,
                'Testimonial_Organization_Name': testimonial.organization_name,
                'Link_to_Video': testimonial.link_to_video
            })

        # Fetch videos created by the person
        videos_data = []
        videos = Video.objects.filter(person=person)
        for video in videos:
            videos_data.append({
                'title': video.title,
                'link': video.link,
                'hd_quality': video.hd_quality,
                'own_rights': video.own_rights,
                'grant_permission': video.grant_permission,
                'reason': video.reason
            })

        response_data = {
            'person_id': serialized_data['id'],
            'email': serialized_data['email'],
            'username': serialized_data['username'],
            'biographies': biographies,
            'manager_or_teammate': manager_or_teammate,
            'speaker_contact_info':speaker_contact_info_data,
            'social_media_personal':social_media_personal_list,
            'fees': fees,
            'images': images,
            'books': all_books_data,
            'degrees_certifications_awards': all_degrees_data,
            'topic_descriptions': topic_descriptions,
            'Brand_Product_CampaignsEndorsementstheme1':brand_campaigns_data1,
            'Brand_Product_CampaignsEndorsementstheme2':brand_campaigns_data2,
            'Help_us_book_you':help_us_book_you_data1,
            'Help_us_work_with_you':help_us_work_with_you_data,
            'at_events': at_events_data,
            'business_info': business_info_data,
            'media_mentions': media_mentions_data,
            'podcasts': podcast_data,
            'previous_clients': previous_clients_data,
            'speaker_pitches': speaker_pitches_data,
            'social_media_business': social_media_business_data,
            'social_media_personal' : social_media_personal_data,
            'white_papers_case_studies': white_papers_case_studies_data,
            'testimonials': testimonials_data,
            'videos': videos_data,
        }

        return Response(response_data, status=200)
    except Person.DoesNotExist:
        return Response({'error': 'Person not found with the specified person_id'}, status=404)
    except Exception as e:
        return Response({'error': str(e)}, status=400)
    
#------------------------------------------------------------------------------------------------------------

@api_view(['GET'])
def get_data_speakertopics(request):
    api_url = "https://speakerscanada.com/json-api/?auth-key=sbcprivatekey&action=topics"

    try:
        response = requests.get(api_url)

        if response.status_code == 200:
            data = response.json()
            return Response(data, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Failed to retrieve data from the external API"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
def get_data_descriptivetitles(request):
    api_url = "https://speakerscanada.com/json-api/?auth-key=sbcprivatekey&action=types"

    try:
        response = requests.get(api_url)

        if response.status_code == 200:
            data = response.json()
            return Response(data, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Failed to retrieve data from the external API"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
