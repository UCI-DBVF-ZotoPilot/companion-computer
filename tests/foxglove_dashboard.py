import asyncio
import json
import math
import time
from foxglove_websocket.server import FoxgloveServer, FoxgloveServerListener

class Listener(FoxgloveServerListener):
    def on_subscribe(self, server: FoxgloveServer, channel_id: int) -> None:
        pass

    def on_unsubscribe(self, server: FoxgloveServer, channel_id: int) -> None:
        pass

    def on_error(self, server: FoxgloveServer, error: Exception) -> None:
        pass

async def generate_mock_data(server: FoxgloveServer): # lidar and camera data mocked for now
    try:
        lidar_channel_id: int = await server.add_channel({
            "topic": "/sensors/lidar",
            "encoding": "json",
            "schemaName": "LidarData",
            "schemaEncoding": "jsonschema",
            "schema": json.dumps({
                "type": "object",
                "properties": {
                    "distance_m": {"type": "number"},
                    "status": {"type": "string"},
                },
            }),
        })
        vision_channel_id: int = await server.add_channel({
            "topic": "/vision/apriltag",
            "encoding": "json",
            "schemaName": "VisionData",
            "schemaEncoding": "jsonschema",
            "schema": json.dumps({
                "type": "object",
                "properties": {
                    "x_offset_px": {"type": "number"},
                    "y_offset_px": {"type": "number"},
                    "z_distance_m": {"type": "number"},
                },
            }),
        })
        start_time: float = time.time()
        
        while True:
            elapsed: float = time.time() - start_time
            lidar_dist: float = max(0.0, 30 - (0.5 * elapsed))
            x_offset: float = 50.0 * math.sin(elapsed)
            y_offset: float = 20.0 * math.cos(elapsed)
            
            await server.send_message(
                lidar_channel_id,
                time.time_ns(),
                json.dumps({"distance_m": lidar_dist, "status": "OK"}).encode("utf8")
            )
            await server.send_message(
                vision_channel_id,
                time.time_ns(),
                json.dumps({
                    "x_offset_px": x_offset, 
                    "y_offset_px": y_offset, 
                    "z_distance_m": lidar_dist
                }).encode("utf8")
            )
            await asyncio.sleep(0.1)
            
    except asyncio.CancelledError:
        pass
    except Exception as e:
        print(f"Error generating mock data: {e}")

async def main(): # initialize server
    try:
        # localhost resolves to ::1 before 127.0.0.1, so listen on both.
        async with FoxgloveServer(["127.0.0.1", "::1"], 8765, "DBVF Mock Server") as server:
            server.set_listener(Listener())
            await generate_mock_data(server)
    except Exception as e:
        print(f"Server initialization failed: {e}")

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass