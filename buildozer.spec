[app]
title = Ultra Injector HS
package.name = ultrainjector
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0
requirements = python3,kivy==2.2.1,pyjnius,android,sdl2,sdl2_image,sdl2_ttf,sdl2_mixer

# الأذونات الضرورية
android.permissions = INTERNET, SYSTEM_ALERT_WINDOW, ACCESS_SUPERUSER

# الإعدادات التقنية للنظام
android.api = 31
android.minapi = 21
android.ndk = 25b
android.archs = arm64-v8a, armeabi-v7a
android.accept_sdk_license = True

# ظهور التطبيق بشكل عمودي
orientation = portrait

[buildozer]
log_level = 2
warn_on_root = 1
