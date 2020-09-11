from pathlib import Path
#Flask Libraries
from flask import Flask, render_template
#ROS Libraries
from ament_index_python.packages import get_package_share_directory
import rclpy
from rclpy.node import Node
from std_msgs.msg import String
app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    map_ = Path(get_package_share_directory('navigation2_agbee'), 'map')
    map_filename = "/home/omose/Desktop/map.pgm" #map_ / 'test.png'
    return render_template("app.html", map_image = map_filename)

class AutonomousAPI(Node):
     def __init__(self):
        super().__init__('autonomous_api')
        self.publisher_ = self.create_publisher(String, 'topic', 10)
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

    def timer_callback(self):
        msg = String()
        msg.data = 'Hello World: %d' % self.i
        self.publisher_.publish(msg)
        self.get_logger(

def main():
    app.run(debug=True)
    rclpy.init(args=args)

    minimal_publisher = MinimalPublisher()

    rclpy.spin(minimal_publisher)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()
