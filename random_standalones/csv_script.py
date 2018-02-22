import csv			

def main():
	read_csv = open('change_csvfile.csv','rb')
	write_csv = open('new_csvfile.csv','wb')
	
	read_contents = csv.reader(read_csv,delimiter=',')
	read_contents_in_rows = list(read_contents)
	read_content_header = read_contents_in_rows[0]
	
	write_file_rows = csv.writer(write_csv,delimiter=',')
	write_file_rows.writerow(['Date','field','field_value'])
	
	for row in read_contents_in_rows[1:]:
		for fields in range(1,len(read_content_header)):
			write_file_rows.writerow( [row[0], read_content_header[fields], row[fields]])

	read_csv.close()
	write_csv.close()
	
if __name__=='__main__':
	main()