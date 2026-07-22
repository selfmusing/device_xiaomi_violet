git clone --depth=1 https://github.com/Justadeayo/platform_vendor_xiaomi_violet.git -b 16 vendor/xiaomi/violet
rm -rf kernel/xiaomi/violet && git clone --depth=1 https://github.com/Justadeayo/android_kernel_xiaomi_violet.git -b sixteen kernel/xiaomi/violet
git clone --depth=1 https://gitlab.com/CuriousNom/chaste_vendor-xiaomi-firmware-violet.git -b 14.0 vendor/xiaomi-firmware/violet
# git clone --depth=1 https://github.com/selfmusing/meme_cam.git -b 15 vendor/MiuiCamera
rm -rf hardware/xiaomi && git clone https://github.com/Evolution-X-Devices/hardware_xiaomi -b bka-no-dolby hardware/xiaomi && rm -rf hardware/xiaomi/packages/DSPVolumeSynchronizer
rm -rf hardware/dolby && git clone https://github.com/adi8900/hardware_dolby -b lunaris hardware/dolby
