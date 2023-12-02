from django.contrib import admin
from .models import (
    Person, Biography, SpeakerTopic, SpeakerTag, DescriptiveTitles, TopicDescription,
    Testimonial, Images, Video, Podcast, Book, MediaMention, WhitePaperCaseStudy,
    DegreesCertificatesAwards, SpeakerContactInformation, ManagerOrTeammate,
    SocialMediaPersonal, BusinessInfo, SocialMediaBusiness, BrandCampaignOrganizationtheme1,
    BrandCampaignOrganizationtheme2, AtEvents, SpeakerIntroduction, HelpUsBookYou,
    HelpUsWorkWithYou, Fees, SpeakerPitch, PreviousClient
)

admin.site.register(Person)
admin.site.register(Biography)
admin.site.register(SpeakerTopic)
admin.site.register(SpeakerTag)
admin.site.register(DescriptiveTitles)
admin.site.register(TopicDescription)
admin.site.register(Testimonial)
admin.site.register(Images)
admin.site.register(Video)
admin.site.register(Podcast)
admin.site.register(Book)
admin.site.register(MediaMention)
admin.site.register(WhitePaperCaseStudy)
admin.site.register(DegreesCertificatesAwards)
admin.site.register(SpeakerContactInformation)
admin.site.register(ManagerOrTeammate)
admin.site.register(SocialMediaPersonal)
admin.site.register(BusinessInfo)
admin.site.register(SocialMediaBusiness)
admin.site.register(BrandCampaignOrganizationtheme1)
admin.site.register(BrandCampaignOrganizationtheme2)
admin.site.register(AtEvents)
admin.site.register(SpeakerIntroduction)
admin.site.register(HelpUsBookYou)
admin.site.register(HelpUsWorkWithYou)
admin.site.register(Fees)
admin.site.register(SpeakerPitch)
admin.site.register(PreviousClient)
