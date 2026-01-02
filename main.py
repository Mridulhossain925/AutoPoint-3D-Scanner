import open3d as o3d
import numpy as np

def load_scan_data(file_path):
    """৩ডি পয়েন্ট ক্লাউড ডাটা লোড করার ফাংশন"""
    try:
        pcd = o3d.io.read_point_cloud(file_path)
        print("Point cloud loaded successfully.")
        return pcd
    except Exception as e:
        print(f"Error loading file: {e}")
        return None

def visualize_scan(pcd):
    """স্ক্যান করা রুমটি ভিউ করার ফাংশন"""
    if pcd is not None:
        print("Opening 3D Viewer... (Close the window to stop)")
        o3d.visualization.draw_geometries([pcd])
    else:
        print("No data to display. Please check your file path.")

if __name__ == "__main__":
    # আপনার এক্সপোর্ট করা .e57 বা .las ফাইলের নাম এখানে দিন
    # উদাহরণ: "my_room.e57"
    file_path = "sample_scan.e57" 
    
    cloud = load_scan_data(file_path)
    visualize_scan(cloud)
