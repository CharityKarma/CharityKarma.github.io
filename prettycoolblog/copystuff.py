import shutil

src = r"""C:\Users\Vegard\Dropbox\programming\Karma2\awesome-karma-blog\_site"""
dst = r"""C:\Users\Vegard\Dropbox\programming\Karma2\CharityKarma.github.io\prettycoolblog"""
assets = r"""\assets"""
shutil.rmtree(dst)
shutil.copytree(src, dst)
#shutil.copytree(src+assets, dst+assets)
