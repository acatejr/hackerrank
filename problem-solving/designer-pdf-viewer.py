def designer_pdf_viewer(h, word):
    letters = "abcdefghijklmnopqrstuvwxyz"
    result = None
    
    if len(word) <= 10:
        heights = []
        for i, c in enumerate(word):
            pos = letters.rfind(c)
            heights.append(h[pos])
        result = max(heights) * len(word)
    
    return result


if __name__ == "__main__":
    h = [1,3,1,3,1,4,1,3,2,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5]
    word = "abc"
    print(designer_pdf_viewer(h, word))


    h = [1,3,1,3,1,4,1,3,2,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,7]
    word = "zaba"
    print(designer_pdf_viewer(h, word))