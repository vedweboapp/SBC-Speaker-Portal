
from . import views
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
# router.register(r'speaker_contact_information/<int:person_id>/', SpeakerContactInformationViewSet),
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
    path('create_person/', views.create_person, name='create_person'),
    path('verify_otp/', views.verify_otp, name='verify_otp'),
    path('login_person/', views.login, name='login'),
    path('stage1/<int:person_id>/', create_speaker_contact_info, name='create-speaker-contact-info'),
    path('stage2/<int:person_id>/', create_biography, name='create-biography'),
    path('stage3/<int:person_id>/', create_topicdescription, name='create_topicdescription'),
    path('stage4/<int:person_id>/', create_image, name='create-image'),
    path('stage5/<int:person_id>/', create_videos, name='create-videos'),
    path('stage6/<int:person_id>/', create_podcasts, name = 'create-podcasts'),
    path('stage7/<int:person_id>/', create_books, name='create-books'),
    path('stage8/<int:person_id>/', create_media_mentions, name='create-media-mentions'),
    path('stage9/<int:person_id>/', create_white_papers_case_studies, name='create-white-papers-case-studies'),
    path('stage10/<int:person_id>/', create_degrees_certifications_awards, name='create_degrees_certifications_awards'),
    path('stage11/<int:person_id>/', create_testimonial, name='create-testimonial'),
    path('stage12/<int:person_id>/', create_business_info, name='create-business-info'),
    path('stage13/<int:person_id>/', create_brand_campaigns, name='create-brand-campaigns'),
    path('stage14/<int:person_id>/', create_at_events, name='create-at-events'),
    path('stage15/<int:person_id>/', create_help_us_book_you, name='create-help-us-book-you'),
    path('stage16/<int:person_id>/', create_help_us_work_with_you, name='create-help-us-work-with-you'),
    path('stage17/<int:person_id>/', create_fees, name='create-fees'),
    path('stage18/<int:person_id>/', create_speaker_pitches, name='create-speaker-pitches'),
    path('stage19/<int:person_id>/', create_previous_clients, name='create-previous-clients'),
    # path('get_files/<filename>/', get_files, name='get_files'),
    path('get_files/<str:filename>/', get_files, name='get_files'),
    path('get_all_data/<int:person_id>/', get_all_data, name='get-all-data'),
    path('get_data_speakertopics/', get_data_speakertopics, name='get_data_speakertopics'),
    path('get_data_descriptivetitles/', get_data_descriptivetitles, name='get_data_descriptivetitles'),






]
from django.conf.urls.static import static

urlpatterns += router.urls

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


