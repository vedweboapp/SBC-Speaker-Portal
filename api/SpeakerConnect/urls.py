from .views import *
from rest_framework import routers
from django.urls import path, include


app_name = "api.SpeakerConnect"

router = routers.DefaultRouter()
router.register(r'speaker_topics', SpeakerTopicViewSet)
router.register(r'biographies', BiographyViewSet)
router.register(r'topic_descriptions', TopicDescriptionViewSet)
router.register(r'testimonials', TestimonialViewSet)
router.register(r'images', ImagesViewSet)
router.register(r'videos', VideoViewSet)
router.register(r'podcasts', PodcastViewSet)
router.register(r'books', BookViewSet)
router.register(r'media_mentions', MediaMentionViewSet)
router.register(r'white_papers_case_studies', WhitePaperCaseStudyViewSet)
router.register(r'degrees_certificates_awards', DegreesCertificatesAwardsViewSet)
router.register(r'speaker_contact_information', SpeakerContactInformationViewSet)
router.register(r'manager_or_teammate', ManagerOrTeammateViewSet)
router.register(r'social_media_personal', SocialMediaPersonalViewSet)
router.register(r'business_info', BusinessInfoViewSet)
router.register(r'social_media_business', SocialMediaBusinessViewSet)
router.register(r'brand_campaign_organization_theme1', BrandCampaignOrganizationtheme1ViewSet)
router.register(r'brand_campaign_organization_theme2', BrandCampaignOrganizationtheme2ViewSet)
router.register(r'at_events', AtEventsViewSet)
router.register(r'speaker_introduction', SpeakerIntroductionViewSet)
router.register(r'help_us_book_you', HelpUsBookYouViewSet)
router.register(r'help_us_work_with_you', HelpUsWorkWithYouViewSet)
router.register(r'fees', FeesViewSet)
router.register(r'speaker_pitch', SpeakerPitchViewSet)
router.register(r'previous_clients', PreviousClientViewSet)
router.register(r'speaker-tags', SpeakerTagViewSet)
router.register(r'descriptive-titles', DescriptiveTitlesViewSet)




urlpatterns = [
    path('api/', include(router.urls)),
]




