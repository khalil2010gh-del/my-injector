import os
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

class InjectorApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=20)
        self.lbl = Label(text="FF INJECTOR\n100% HEADSHOT ANY PART", font_size='20sp', halign='center')
        btn = Button(text="ACTIVATE NOW", size_hint_y=None, height='100dp', background_color=(1, 0, 0, 1))
        btn.bind(on_press=self.inject)
        layout.add_widget(self.lbl)
        layout.add_widget(btn)
        return layout

    def inject(self, instance):
        # الكود الذي سيتم إرساله لنظام الأندرويد داخل الناسخ
        pkg = "com.dts.freefireth"
        offset = "0x14D9A20"
        value = "\\x00\\x00\\x80\\x43"
        
        # أمر الحقن باستخدام صلاحيات الروت
        cmd = f"su -c 'PID=$(pidof {pkg}); BASE=$(grep \"libil2cpp.so\" /proc/$PID/maps | head -n 1 | cut -d \"-\" -f1); printf \"{value}\" | dd of=/proc/$PID/mem bs=1 seek=$((0x$BASE + {offset})) conv=notrunc 2>/dev/null'"
        
        os.system(cmd)
        self.lbl.text = "✅ SUCCESS! GOTO GAME"

if __name__ == "__main__":
    InjectorApp().run()
