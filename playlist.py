# 以播放列表與聲音為例覆寫運算子

class Playable:
    def __init__(self, title: str, dursion: int) -> None:
        self.title = title
        self.dursion = dursion
    def describe(self) -> str:
        return self.title
    def __str__(self) -> str:
        mins = self.dursion // 60
        secs = self.dursion % 60
        return f"{self.describe()} {mins}:{secs:02}"

class Song(Playable):
    def __init__(self, title: str, dursion: int, artist: str) -> None:
        super().__init__(title, dursion)
        self.artist = artist
    def describe(self) -> str:
        return f"[{self.artist} - {self.title}]"

class Podcast(Playable):
    def __init__(self, title: str, dursion: int, episode: int) -> None:
        super().__init__(title, dursion)
        self.episode = episode
    def describe(self) -> str:
        return f"[{self.title} v.{self.episode}]"

class AudioBook(Playable):
    def __init__(self, title: str, dursion: int, chapter: str) -> None:
        super().__init__(title, dursion)
        self.chapter = chapter
    def describe(self) -> str:
        return f"{self.title}({self.chapter})"


sound01 = Song("龍捲風", 212, "周杰倫")
sound02 = Podcast("台灣通行第一品牌", 1800, 242)
sound03 = AudioBook("轉生史萊姆", 36007, "第一集第一章")

print(sound01)
print(sound02)
print(sound03)
