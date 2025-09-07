import requests
from tqdm import tqdm

# 播放列表标题
titles = [
    "徽宗即位","奸相辅政","宦官掌兵","风流天子","靖康之变","康王赵构","赵构继统",
    "书生抗金","逃跑皇帝","苗刘兵变","韩五破金","将帅失和","吴玠守蜀","精忠岳飞",
    "傀儡刘豫","伪齐灭亡","中兴四将","君臣反目","淮西军变","宋金谈判","战端再起",
    "顺昌大捷","功亏一篑","死里逃生","岳飞之死","宋金和议","奸相秦桧","金国易主",
    "宋金再战","高宗禅位"
]

base_url = "https://down01.pingshu8888.com:8011/2/zy/liangsongfengyun/{index}.mp3"

# 浏览器模拟请求头
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36",
    "Referer": "https://down01.pingshu8888.com/"
}

total_files = len(titles)

for i, title in enumerate(titles, start=1):
    index_str = f"{i:02d}"
    url = base_url.format(index=index_str)
    filename = f"{i}.{title}.mp3"

    try:
        # 发请求，获取内容长度
        with requests.get(url, headers=headers, stream=True) as r:
            r.raise_for_status()
            total_size = int(r.headers.get('content-length', 0))
            chunk_size = 1024*1024  # 1MB

            # tqdm 显示当前文件下载进度
            with tqdm(total=total_size, unit='B', unit_scale=True,
                      desc=f"[{i}/{total_files}] {filename}") as pbar:
                with open(filename, "wb") as f:
                    for chunk in r.iter_content(chunk_size=chunk_size):
                        if chunk:
                            f.write(chunk)
                            pbar.update(len(chunk))
    except Exception as e:
        print(f"下载失败: {filename}, 错误: {e}")

print("全部下载完成！")
