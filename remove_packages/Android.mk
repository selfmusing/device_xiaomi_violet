LOCAL_PATH := $(call my-dir)

include $(CLEAR_VARS)
LOCAL_MODULE := RemovePkgs
LOCAL_MODULE_CLASS := APPS
LOCAL_MODULE_TAGS := optional

LOCAL_OVERRIDES_PACKAGES := \
    AmbientSensePrebuilt \
    AmbientStreaming \
    AppDirectedSMSService \
    CalculatorGooglePrebuilt_85006267 \
    CalendarGooglePrebuilt \
    ConnMO \
    Contacts \
    DCMO \
    DeskClock \
    DevicePolicyPrebuilt-v10334460 \
    Dialer \
    DMService \
    Drive \
    Etar \
    FamilyLinkParentalControls \
    Flash \
    Gallery2 \
    GCS \
    GeminiShell_227 \
    Gmail2 \
    Glimpse \
    GoogleCamera \
    GoogleContacts \
    HealthIntelligenceStubPrebuilt \
    Jelly \
    KidsSupervisionStub \
    MaestroPrebuilt \
    Maps \
    Messaging \
    MlkitBarcodeUIPrebuilt \
    MyVerizonServices \
    obdm_stub \
    OBDM_Permissions \
    OdadPrebuilt \
    Photos \
    PixelSupportPrebuilt \
    PlayAutoInstallConfig \
    PrebuiltPixelCoreServices \
    RelationshipsPrebuilt-301 \
    SafetyHubPrebuilt \
    SCONE \
    ScribePrebuilt_v8.4.773573318 \
    SearchSelectorPrebuilt \
    SettingsIntelligence \
    Showcase \
    Snap \
    SoundAmplifierPrebuilt_v4.8.758106410 \
    SprintDM \
    SprintHM \
    SwitchAccessPrebuilt_1.16.0.726766860 \
    talkback \
    Tycho \
    UdfpsAnimations \
    UdfpsIcons \
    USCCDM \
    VisionBarcodePrebuilt \
    VZWAPNLib \
    VzwOmaTrigger \
    YouTube \
    YouTubeMusicPrebuilt

LOCAL_UNINSTALLABLE_MODULE := true
LOCAL_CERTIFICATE := platform
LOCAL_SRC_FILES := /dev/null
include $(BUILD_PREBUILT)