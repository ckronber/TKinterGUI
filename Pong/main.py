from kivy.app import App
from kivy.uix.widget import Widget
from kivy.vector import Vector
from kivy.properties import NumericProperty, ReferenceListProperty,ObjectProperty
from kivy.clock import Clock

class PongGame(Widget):
    def update(self, dt):
        #call ball.move and other stuff
        pass

class PongBall(Widget):
    #velocity of the ball on x and y axis
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)

    #referencelist property so we can use ball.velocity as
    # a shorthand, just like e.g. w.pos for w.x and w.y
    velocity = ReferenceListProperty(velocity_x, velocity_y)

    # ''move'' function will move the ball one step. This
    # will mbe cancelled in equal intervals to animate the ball
    def move(self):
        self.pos = Vector(*self.velocity)+self.pos

class PongApp(App):
    def build(self):
        game = PongGame()
        Clock.schedule_interval(game.update, 1.0/60.0)

if __name__ == '__main__':
    PongApp().run()