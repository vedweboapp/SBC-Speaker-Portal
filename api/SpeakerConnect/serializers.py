from rest_framework import serializers
from SpeakerConnect.models import *


class SpeakerTopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpeakerTopic
        fields = '__all__'


class BiographySerializer(serializers.ModelSerializer):
    class Meta:
        model = Biography
        fields = '__all__'


class TopicDescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TopicDescription
        fields = '__all__'


class TestimonialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonial
        fields = '__all__'


class ImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Images
        fields = '__all__'


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = '__all__'


class PodcastSerializer(serializers.ModelSerializer):
    class Meta:
        model = Podcast
        fields = '__all__'


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


class MediaMentionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MediaMention
        fields = '__all__'


class WhitePaperCaseStudySerializer(serializers.ModelSerializer):
    class Meta:
        model = WhitePaperCaseStudy
        fields = '__all__'


class DegreesCertificatesAwardsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DegreesCertificatesAwards
        fields = '__all__'


class SpeakerContactInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpeakerContactInformation
        fields = '__all__'


class ManagerOrTeammateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ManagerOrTeammate
        fields = '__all__'


class SocialMediaPersonalSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialMediaPersonal
        fields = '__all__'


class BusinessInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusinessInfo
        fields = '__all__'


class SocialMediaBusinessSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialMediaBusiness
        fields = '__all__'


class BrandCampaignOrganizationtheme1Serializer(serializers.ModelSerializer):
    class Meta:
        model = BrandCampaignOrganizationtheme1
        fields = '__all__'


class BrandCampaignOrganizationtheme2Serializer(serializers.ModelSerializer):
    class Meta:
        model = BrandCampaignOrganizationtheme2
        fields = '__all__'


class AtEventsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AtEvents
        fields = '__all__'


class SpeakerIntroductionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpeakerIntroduction
        fields = '__all__'


class HelpUsBookYouSerializer(serializers.ModelSerializer):
    class Meta:
        model = HelpUsBookYou
        fields = '__all__'


class HelpUsWorkWithYouSerializer(serializers.ModelSerializer):
    class Meta:
        model = HelpUsWorkWithYou
        fields = '__all__'


class FeesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fees
        fields = '__all__'


class SpeakerPitchSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpeakerPitch
        fields = '__all__'


class PreviousClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = PreviousClient
        fields = '__all__'

class SpeakerTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpeakerTag
        fields = '__all__'

class DescriptiveTitlesSerializer(serializers.ModelSerializer):
    class Meta:
        model = DescriptiveTitles
        fields = '__all__'