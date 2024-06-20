import setuptools 

with open("README.md", "r") as fh: 
	long_description = fh.read() 

setuptools.setup( 
	# Here is the module name. 
	name="PineUtils", 

	# version of the module 
	version="0.0.5", 

	# Name of Author 
	author="Plaraje (DMAM2)", 

	# your Email address 
	author_email="plaraje@proton.me", 


	# long_description=long_description, 

	# Specifying that we are using markdown file for description 
	long_description=long_description, 
	long_description_content_type="text/markdown", 

	# Any link to reach this module, ***if*** you have any webpage or github profile 
	url="https://github.com/plaraje/PineUtils", 
	packages=setuptools.find_packages(), 




    install_requires=[ 
        "Chromify", 
    ], 


	license="GNU AFFERO GENERAL PUBLIC LICENSE", 

	# classifiers like program is suitable for python3, just leave as it is. 
	classifiers=[ 
		"Programming Language :: Python :: 3", 
		"Operating System :: OS Independent", 
	], 
) 
