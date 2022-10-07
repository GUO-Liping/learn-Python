from PIL import Image as ImagePIL
import os

def transfer(infile, outfile):
	im = ImagePIL.open(infile)
	width, height = im.width, im.height
	if width == height:
		set_width = 5.0  # 5.0 cm
	elif width > height:
		set_width = 7.5  # 7.5 cm
	set_dpi = 300  # 300 pixel/inch
	dpi_w = int(set_width/2.54*set_dpi)  # 1 inch = 2.54 cm, dpi = 300dpi/inch, when figwidth=7.5cm
	dpi_h = int(dpi_w*height/width)
	im = im.resize((dpi_w,dpi_h))  # (896,560)
	print(im.format, im.size, im.mode,width, height)
	im=im.convert('RGB')
	im.save(outfile, dpi=(set_dpi, set_dpi)) #想要设定的dpi值

if __name__ == '__main__':
	for root, dirs, files in os.walk("chapter2_figs\\"): ##ori_ img为需要修改的图片存储的文件夹名字
		for item in files:
			list = item. split(".")
			print(list[-1])
			if(list[-1] == "png"):
				#os.rename("chapter2_figsQ\\" + item, "chapter2_figsQ\\" + list[0] + ".png")
				new_name = list[0] + ".jpg"
				transfer("chapter2_figs\\" + item, "chapter2_figs_dpi\\" + new_name )
			elif(list[-1] == "jpg"):
				new_name = list[0] + ".jpg"
				transfer("chapter2_figs\\" + item, "chapter2_figs_dpi\\" + new_name )
			else:
				pass
