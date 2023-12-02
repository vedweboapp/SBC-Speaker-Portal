from rest_framework import viewsets
from .serializers import *

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