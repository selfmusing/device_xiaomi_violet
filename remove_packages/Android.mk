LOCAL_PATH := $(call my-dir)

include $(CLEAR_VARS)
LOCAL_MODULE := RemovePkgs
LOCAL_MODULE_CLASS := APPS
LOCAL_MODULE_TAGS := optional
LOCAL_OVERRIDES_PACKAGES := AmbientSensePrebuilt Chrome-Stub AmbientStreaming AppDirectedSMSService Drive Chrome ConnMO OdadPrebuilt CalculatorGooglePrebuilt DCMO CalendarGooglePrebuilt
LOCAL_OVERRIDES_PACKAGES += DMService GCS GoogleCamera HealthIntelligenceStubPrebuilt KidsSupervisionStub MaestroPrebuilt Maps MyVerizonServices
LOCAL_OVERRIDES_PACKAGES += YouTube YouTubeMusicPrebuilt SafetyHubPrebuilt SCONE ScribePrebuilt Showcase Snap Photos PixelSupportPrebuilt PlayAutoInstallConfig SwitchAccessPrebuilt PrebuiltGmail
LOCAL_OVERRIDES_PACKAGES += SoundAmplifierPrebuilt SprintDM SprintHM talkback TurboPrebuilt Tycho USCCDM VZWAPNLib Flash
LOCAL_OVERRIDES_PACKAGES += VzwOmaTrigger VoiceAccessPrebuilt OBDM_Permissions obdm_stub DevicePolicyPrebuilt
LOCAL_UNINSTALLABLE_MODULE := true
LOCAL_CERTIFICATE := platform
LOCAL_SRC_FILES := /dev/null
include $(BUILD_PREBUILT)
