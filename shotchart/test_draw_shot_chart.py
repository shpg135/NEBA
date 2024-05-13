from PIL import Image, ImageDraw, ImageFont

# 加载图片
image_path = 'nbahalfcourt.png'  # 假设图片和脚本在同一目录下
image = Image.open(image_path)
draw = ImageDraw.Draw(image)

# 假设你有一个包含投篮数据的列表
shots = [
    (100, 200, 'miss'),
    (110, 180, 'make'),
    (120, 170, 'make'),
]

# 标记的符号和颜色
mark_miss = 'x'
mark_make = 'o'
color_miss = 'red'
color_make = 'green'

# 字体设置（可选，如果你想要显示文本而不是只显示符号）
font = ImageFont.truetype('arial.ttf', 15)  # 使用系统字体，你可能需要更改路径或字体名

# 遍历投篮数据并绘制标记
for x, y, result in shots:
    if result == 'make':
        draw.text((x, y), mark_make, fill=color_make, font=font)
        #draw.text((x, y), mark_make, fill=color_make)
        # 或者如果你只想绘制符号而不添加文本，可以使用：
        # draw.point((x, y), fill=color_make)
    elif result == 'miss':
        draw.text((x, y), mark_miss, fill=color_miss, font=font)
        #draw.text((x, y), mark_miss, fill=color_miss)
        # 或者如果你只想绘制符号而不添加文本，可以使用：
        # draw.point((x, y), fill=color_miss)

# 保存修改后的图片
output_path = 'marked_court.png'
image.save(output_path)

# 显示图片（可选，如果你在一个支持图像显示的环境中运行此代码）
image.show()