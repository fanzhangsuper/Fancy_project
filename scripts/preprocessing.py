# import pyspark
def _remove_line_breaks(list_of_strings):
    for i, s in enumerate(list_of_strings):
        if s.endswith('\\\n'):
            list_of_strings[i] = s[:-2]

        if i % 10000 == 0:
        	print("Iter " + str(i))


def preprocessing_data(file_path, new_path):
	with open(file_path, 'r') as h:
	    lines = h.readlines()

	print("length of the lines = ", len(lines))

	_remove_line_breaks(lines)

	with open(new_path, 'w') as h:
	    h.writelines(lines)

	print("file has been written successfully.")

if __name__ == '__main__':
	import os
	print(os.getcwd())
	# sc = pyspark.SparkContext()
	# a = sc.textFile("hdfs:/datasets/twitter-swisscom/sample.tsv")
	# print(len(a.count()))
