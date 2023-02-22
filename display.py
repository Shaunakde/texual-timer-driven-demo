import asyncio
from textual import log
from textual.app import App, ComposeResult
from textual.containers import Content
from textual.widgets import Input, Label
import time

class UpdateOnTimer(App):
    # This is called to structure the widgets in the screen (Default Screen)
    def compose(self) -> ComposeResult:
        self.center_label = Label(id="label")
        yield self.center_label
        yield Input(placeholder="Current Time", id="text-box")

    # Run at app startup 
    def on_mount(self):
        # Styles
        self.center_label.styles.height="0.1fr"
        #self.center_label.styles.outline = ("solid", "yellow")
        # Initialize the components
        self.query_one("#label").update("UTC Time")
        self.query_one("#text-box").focus()
        self.set_interval(1.0, callback=self.lookup_time, name="MainTimer")

    async def lookup_time(self) -> None:
        asyncio.sleep(1)
        date_time = time.strftime("%a, %d %b %Y %H:%M:%S +0000", time.gmtime())
        log(f"Updating {date_time}")
        self.query_one("#text-box").action_end()
        self.query_one("#text-box").action_delete_left_all()
        self.query_one("#text-box").insert_text_at_cursor(f"{date_time}")
        return
        
if __name__=="__main__":
    app = UpdateOnTimer()    
    app.run()
