import subprocess
import datetime

url = "http://[2409:8087:1:20:20::2c]/otttv.bj.chinamobile.com/PLTV/88888888/224/3221226895/1.m3u8?GuardEncType=2&accountinfo=~%7EV2.0%7EI0Rkc6neBYgfpoJ1yud8Fw%7E_eNUbgU9sJGUcVVduOMKhafLvQUgE_zlz_7pvDimJNPpqgHe3PQ5GNQoO-yUgA8C%2CEND"
log_filename = f"ffmpeg_log_{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}.log"

command = [
    "ffmpeg",
    "-i", url,
    "-t", "25",        # 运行25秒
    "-c", "copy",      # 不重新编码
    "-f", "null",      # 不输出文件
    "-loglevel", "debug",  # 记录详细日志
    "-"                # 输出到空设备
]

with open(log_filename, "w") as log_file:
    process = subprocess.run(
        command,
        stderr=log_file,
        text=True
    )

print("FFmpeg 执行完成，日志已保存至:", log_filename)