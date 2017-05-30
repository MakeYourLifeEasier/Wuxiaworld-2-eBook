import links
import getify

print (links.index())

# Gets the choise of novels and chapters
novel = input("Which Novel do you want to read? (Enter a number): ")
novel = int(novel)
book = 0
if novel == 11 or novel == 18 or novel == 25 or novel == 40 or novel == 44 or novel == 45 or novel == 49:
	book = input("Which Book do you want to read?")
raw_info = links.info(novel, book)
s_chapter = input("What chapter do you want to start at?: ")
f_chapter = s_chapter
s_chapter = int(s_chapter)
x_chapter = s_chapter
e_chapter = input("Till what chapter do you want to read?: ")
end_chapter = e_chapter
e_chapter = int(e_chapter)

# Generates Link list
bulk_list = []
for s_chapter in range(s_chapter, e_chapter + 1):
	s_chapter_string = str(s_chapter)
	bulk_list.append(raw_info["link"] + s_chapter_string)

#Does the calls for downloadingand modifying
#and the progress bar... Don't forget the progress bar
array_length = len(bulk_list)
file_list = []
for x in range(array_length):
	x_chapter = str(x_chapter)
	getify.download(bulk_list[x], x_chapter + ".xhtml")
	getify.clean(x_chapter + ".xhtml", raw_info["ChapterName"] + x_chapter, '<div itemprop="articleBody"', '''<div class='code-block''')
	file_list.append(raw_info["ChapterName"] + x_chapter + ".xhtml")
	x_chapter = int(x_chapter)
	x_chapter += 1
	getify.update_progress(x/array_length)

#Generates the eBook
print("")
print("Creating ePub...")
getify.generate(file_list, raw_info["NovelName"], raw_info["author"], raw_info["ChapterName"], f_chapter, end_chapter)

print ("Success . . . Hopefully")
