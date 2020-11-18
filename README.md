# pytubeGUI
PytubeGUI is a graphical user interface created with Python's Tkinter library. The application downloads videos in 720p resoulution from youtube using the pytube module https://pypi.org/project/pytube/. 

## Usage

```python
# Create function to take a search for user input
def submitURL(url):

    try:
        # Create youtube object with user URL
        global yt
        yt =YouTube(url)
        showYTTitle =  yt.title
        
        youTubeTitle = Label(initialWindow, 
        text=showYTTitle, 
        font =("Arial", 16)
        )
        youTubeTitle.pack()

            # break out of the while loop if title is real
    except pytube.exceptions.RegexMatchError:
            # Create error message in window so user knows what went wrong
        titleError = Label(initialWindow, 
        text="Please enter correct URL from YouTube.com "
        )
        titleError.pack()

```
