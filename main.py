import os
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock

class MultiAppInjector(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', padding=20, spacing=15)
        
        self.lbl = Label(
            text="MULTI-APP INJECTOR V3\n[ MODE: VIRTUAL ROOT ]", 
            font_size='18sp', 
            color=(1, 1, 0, 1),
            halign='center'
        )
        
        self.btn = Button(
            text="ACTIVATE 100% HS\n(ANY PART = HEAD)",
            background_color=(0.1, 0.5, 0.8, 1),
            size_hint_y=None, height='90dp',
            font_size='20sp'
        )
        self.btn.bind(on_press=self.start_virtual_injection)
        
        self.layout.add_widget(self.lbl)
        self.layout.add_widget(self.btn)
        return self.layout

    def start_virtual_injection(self, instance):
        self.lbl.text = "Searching in Multi App environment..."
        # تأخير بسيط لضمان استقرار الناسخ
        Clock.schedule_once(self.run_injection, 1.5)

    def run_injection(self, dt):
        pkg = "com.dts.freefireth"
        # أوفست الهيتبوكس (تحويل الجسم لرأس)
        offset = "0x14D9A20"
        value = "\\x00\\x00\\x80\\x43"
        
        # أمر حقن مخصص للعمل داخل النواسخ (يعتمد على su الموجود في الناسخ)
        # أضفنا 2>/dev/null لتجنب رسائل الخطأ التي قد تعطل التطبيق
        cmd = f"""
        su -c '
        PID=$(pidof {pkg})
        if [ -z "$PID" ]; then
            # محاولة البحث عن العملية في حال كان اسم الحزمة مختلف داخل الناسخ
            PID=$(ps -ef | grep {pkg} | grep -v grep | awk "{{print $2}}" | head -n 1)
        fi
        
        if [ ! -z "$PID" ]; then
            BASE=$(grep "libil2cpp.so" /proc/$PID/maps | head -n 1 | cut -d "-" -f1)
            if [ ! -z "$BASE" ]; then
                printf "{value}" | dd of=/proc/$PID/mem bs=1 seek=$((0x$BASE + {offset})) conv=notrunc 2>/dev/null
                echo "DONE"
            fi
        fi'
        """
        
        # تنفيذ الأمر
        result = os.system(cmd)
        
        if result == 0:
            self.lbl.text = "✅ SUCCESS!\nHeadshot Enabled in Multi App"
            self.lbl.color = (0, 1, 0, 1)
        else:
            self.lbl.text = "❌ ERROR\nMake sure Multi-App has Root/64bit support"
            self.lbl.color = (1, 0, 0, 1)

if __name__ == "__main__":
    MultiAppInjector().run()
