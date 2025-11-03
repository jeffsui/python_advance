"""
windows notification demo
python实现windows通知栏消息
"""

from winotify import Notification, audio

toast = Notification(
    app_id=r"{1AC14E77-02E7-4E5D-B744-2EB1AE5198B7}\SnippingTool.exe",  # 绑定程序，否则无法显示图标
    title="屏幕截图已复制到粘贴板",  # 标题
    msg="您已成功将截图复制到剪贴板。",  # 内容
    duration="short",  # 通知持续时间
    icon="",  # 通知栏左侧图标
    launch="",  # 点击通知栏打开的程序
)
toast.add_actions(label="查看截图", launch="")  # 添加按钮
# add audio
toast.set_audio(audio.Default, loop=False)  # 设置通知音频
toast.show()
