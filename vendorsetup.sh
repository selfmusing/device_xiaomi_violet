git clone --depth=1 https://github.com/selfmusing/vendor_xiaomi_violet.git -b udc vendor/xiaomi/violet
git clone --depth=1 https://github.com/selfmusing/kernel_xiaomi_violet.git -b main kernel/xiaomi/violet
git clone --depth=1 https://gitlab.com/CuriousNom/chaste_vendor-xiaomi-firmware-violet.git -b 14.0 vendor/xiaomi-firmware/violet
git clone --depth=1 https://gitlab.com/kibria5/android_vendor_MiuiCamera -b 14 vendor/MiuiCamera
git clone https://github.com/selfmusing/vendor_bcr vendor/bcr
git clone https://github.com/DerpFest-Devices/hardware_xiaomi -b 14 hardware/xiaomi
rm -rf prebuilts/clang/host/linux-x86/clang-r522817 && git clone --depth=1 https://gitlab.com/itsshashanksp/android_prebuilts_clang_host_linux-x86_clang-r522817.git -b 14.0 prebuilts/clang/host/linux-x86/clang-r522817 
