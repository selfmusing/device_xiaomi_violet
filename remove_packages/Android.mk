LOCAL_PATH := $(call my-dir)

include $(CLEAR_VARS)
LOCAL_MODULE := RemovePkgs
LOCAL_MODULE_CLASS := APPS
LOCAL_MODULE_TAGS := optional
LOCAL_OVERRIDES_PACKAGES := AmbientSensePrebuilt AmbientStreaming AppDirectedSMSService Drive ConnMO OdadPrebuilt CalculatorGoogle DCMO CalendarGoogle
LOCAL_OVERRIDES_PACKAGES += DMService GCS GoogleCamera HealthIntelligenceStubPrebuilt KidsSupervisionStub MaestroPrebuilt Maps MyVerizonServices EmergencyInfoGms
LOCAL_OVERRIDES_PACKAGES += YouTube YouTubeMusicPrebuilt SafetyHubPrebuilt SCONE ScribePrebuilt Showcase Snap Photos PixelSupportPrebuilt PlayAutoInstallConfig SwitchAccessPrebuilt Gmail2 FamilyLinkParentalControls PersonalSafety
LOCAL_OVERRIDES_PACKAGES += SoundAmplifierPrebuilt SprintDM SprintHM talkback Tycho USCCDM VZWAPNLib Flash
LOCAL_OVERRIDES_PACKAGES += VzwOmaTrigger VoiceAccessPrebuilt OBDM_Permissions obdm_stub DevicePolicyPrebuilt
LOCAL_UNINSTALLABLE_MODULE := true
LOCAL_CERTIFICATE := platform
LOCAL_SRC_FILES := /dev/null
include $(BUILD_PREBUILT)
