# Copyright (C) 2009 The Android Open Source Project
# Copyright (c) 2011, The Linux Foundation. All rights reserved.
# Copyright (C) 2017-2020 The LineageOS Project
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import common
import re

def FullOTA_InstallBegin(info):
  input_zip = info.input_zip
  AddImage(info, "RADIO", input_zip, "super_dummy.img", "/tmp/super_dummy.img");
  info.script.AppendExtra('package_extract_file("install/bin/flash_super_dummy.sh", "/tmp/flash_super_dummy.sh");')
  info.script.AppendExtra('set_metadata("/tmp/flash_super_dummy.sh", "uid", 0, "gid", 0, "mode", 0755);')
  info.script.AppendExtra('run_program("/tmp/flash_super_dummy.sh");')
  return

def FullOTA_InstallEnd(info):
  input_zip = info.input_zip
  OTA_UpdateFirmware(info)
  OTA_InstallEnd(info, input_zip)
  return

def IncrementalOTA_InstallEnd(info):
  input_zip = info.target_zip
  OTA_UpdateFirmware(info)
  OTA_InstallEnd(info, input_zip)
  return

def OTA_UpdateFirmware(info):
  info.script.AppendExtra('ui_print("Flashing firmware images");')
  info.script.AppendExtra('package_extract_file("install/firmware-update/abl.elf", "/dev/block/bootdevice/by-name/abl");')
  info.script.AppendExtra('package_extract_file("install/firmware-update/abl.elf", "/dev/block/bootdevice/by-name/ablbak");')
  info.script.AppendExtra('package_extract_file("install/firmware-update/aop.mbn", "/dev/block/bootdevice/by-name/aop");')
  info.script.AppendExtra('package_extract_file("install/firmware-update/BTFM.bin", "/dev/block/bootdevice/by-name/bluetooth");')
  info.script.AppendExtra('package_extract_file("install/firmware-update/imagefv.elf", "/dev/block/bootdevice/by-name/imagefv");')
  info.script.AppendExtra('package_extract_file("install/firmware-update/imagefv.elf", "/dev/block/bootdevice/by-name/imagefvbak");')
  info.script.AppendExtra('package_extract_file("install/firmware-update/cmnlib.mbn", "/dev/block/bootdevice/by-name/cmnlib");')
  info.script.AppendExtra('package_extract_file("install/firmware-update/cmnlib.mbn", "/dev/block/bootdevice/by-name/cmnlibbak");')
  info.script.AppendExtra('package_extract_file("install/firmware-update/cmnlib64.mbn", "/dev/block/bootdevice/by-name/cmnlib64");')
  info.script.AppendExtra('package_extract_file("install/firmware-update/cmnlib64.mbn", "/dev/block/bootdevice/by-name/cmnlib64bak");')
  info.script.AppendExtra('package_extract_file("install/firmware-update/devcfg.mbn", "/dev/block/bootdevice/by-name/devcfg");')
  info.script.AppendExtra('package_extract_file("install/firmware-update/devcfg.mbn", "/dev/block/bootdevice/by-name/devcfgbak");')
  info.script.AppendExtra('package_extract_file("install/firmware-update/dspso.bin", "/dev/block/bootdevice/by-name/dsp");')
  info.script.AppendExtra('package_extract_file("install/firmware-update/hyp.mbn", "/dev/block/bootdevice/by-name/hyp");')
  info.script.AppendExtra('package_extract_file("install/firmware-update/hyp.mbn", "/dev/block/bootdevice/by-name/hypbak");')
  info.script.AppendExtra('package_extract_file("install/firmware-update/km4.mbn", "/dev/block/bootdevice/by-name/keymaster");')
  info.script.AppendExtra('package_extract_file("install/firmware-update/km4.mbn", "/dev/block/bootdevice/by-name/keymasterbak");')
  info.script.AppendExtra('package_extract_file("install/firmware-update/splash.img", "/dev/block/bootdevice/by-name/splash");')
  info.script.AppendExtra('package_extract_file("install/firmware-update/NON-HLOS.bin", "/dev/block/bootdevice/by-name/modem");')
  info.script.AppendExtra('package_extract_file("install/firmware-update/qupv3fw.elf", "/dev/block/bootdevice/by-name/qupfw");')
  info.script.AppendExtra('package_extract_file("install/firmware-update/qupv3fw.elf", "/dev/block/bootdevice/by-name/qupfwbak");')
  info.script.AppendExtra('package_extract_file("install/firmware-update/storsec.mbn", "/dev/block/bootdevice/by-name/storsec");')
  info.script.AppendExtra('package_extract_file("install/firmware-update/storsec.mbn", "/dev/block/bootdevice/by-name/storsecbak");')
  info.script.AppendExtra('package_extract_file("install/firmware-update/uefi_sec.mbn", "/dev/block/bootdevice/by-name/uefisecapp");')
  info.script.AppendExtra('package_extract_file("install/firmware-update/uefi_sec.mbn", "/dev/block/bootdevice/by-name/uefisecappbak");')
  info.script.AppendExtra('package_extract_file("install/firmware-update/tz.mbn", "/dev/block/bootdevice/by-name/tz");')
  info.script.AppendExtra('package_extract_file("install/firmware-update/tz.mbn", "/dev/block/bootdevice/by-name/tzbak");')
  info.script.AppendExtra('package_extract_file("install/firmware-update/xbl.elf", "/dev/block/bootdevice/by-name/xbl");')
  info.script.AppendExtra('package_extract_file("install/firmware-update/xbl.elf", "/dev/block/bootdevice/by-name/xblbak");')
  info.script.AppendExtra('package_extract_file("install/firmware-update/xbl_config.elf", "/dev/block/bootdevice/by-name/xbl_config");')

def AddBasebandAssertion(info, input_zip):
  android_info = input_zip.read("OTA/android-info.txt")
  variants = []
  for variant in ('in', 'cn', 'eea'):
    result = re.search(r'require\s+version-{}\s*=\s*(\S+)'.format(variant), android_info.decode('utf-8'))
    if result is not None:
      variants.append(result.group(1).split(','))
  cmd = 'assert(getprop("ro.boot.hwc") == "{0}" && (xiaomi.verify_baseband("{2}", "{1}") == "1" || abort("ERROR: This package requires baseband from atleast {2}. Please upgrade firmware and retry!");) || true);'
  for variant in variants:
    info.script.AppendExtra(cmd.format(*variant))

def AddImage(info, dir, input_zip, basename, dest):
  name = basename
  path = dir + "/" + name
  if path not in input_zip.namelist():
    return

  data = input_zip.read(path)
  common.ZipWriteStr(info.output_zip, name, data)
  info.script.Print("Patching {} image unconditionally...".format(dest.split('/')[-1]))
  info.script.AppendExtra('package_extract_file("%s", "%s");' % (name, dest))

def OTA_InstallEnd(info, input_zip):
  AddImage(info, "IMAGES", input_zip, "vbmeta.img", "/dev/block/bootdevice/by-name/vbmeta")
  AddImage(info, "IMAGES", input_zip, "vbmeta_system.img", "/dev/block/bootdevice/by-name/vbmeta_system")
  AddImage(info, "IMAGES", input_zip, "dtbo.img", "/dev/block/bootdevice/by-name/dtbo")
  return
