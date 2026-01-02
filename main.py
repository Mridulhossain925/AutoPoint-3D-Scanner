import open3d as o3d
import numpy as np
import os

class AutoPointScanner:
    def __init__(self, file_path):
        self.file_path = file_path
        self.point_cloud = None

    def load_data(self):
        """ফাইল লোড করার ফাংশন (.e57, .las, .ply সাপোর্ট করবে)"""
        if not os.path.exists(self.file_path):
            print(f"Error: ফাইলটি পাওয়া যায়নি -> {self.file_path}")
            return False
        
        print("Loading 3D Data... Please wait.")
        # Open3D দিয়ে ডাটা রিড করা
        self.point_cloud = o3d.io.read_point_cloud(self.file_path)
        
        if self.point_cloud.is_empty():
            print("Error: ফাইলে কোনো ডাটা নেই!")
            return False
        
        print(f"Success: {len(self.point_cloud.points)} টি পয়েন্ট লোড হয়েছে।")
        return True

    def remove_nadir_mask(self):
        """
        কালো মাস্ক সরানোর প্রাথমিক লজিক।
        এটি স্ক্যানারের খুব কাছের (যেখানে মানুষ থাকে) পয়েন্টগুলো ফিল্টার করবে।
        """
        # স্ক্যানার থেকে ০.৫ মিটারের ভেতরের পয়েন্টগুলো বাদ দেওয়া (অপারেটর মাস্ক)
        points = np.asarray(self.point_cloud.points)
        distances = np.linalg.norm(points, axis=1)
        mask = distances > 0.5  # ০.৫ মিটারের বেশি দূরের পয়েন্ট রাখা
        self.point_cloud.points = o3d.utility.Vector3dVector(points[mask])
        print("Operator mask filtered.")

    def generate_virtual_setup_point(self, new_location=[1.0, 1.0, 1.5]):
        """
        অটোমেটিক নতুন সেটআপ পয়েন্ট তৈরির ফ্রেমওয়ার্ক।
        এখানে নতুন কোঅর্ডিনেট দিলে সেখান থেকে ভিউ জেনারেট হবে।
        """
        print(f"Generating Virtual Setup Point at: {new_location}")
        # এই ফিচারে আমরা ভবিষ্যতে AI Inpainting যোগ করব
        pass

    def run_viewer(self):
        """৩ডি ভিউয়ার ওপেন করবে যেখানে সব দিক দেখা যাবে"""
        if self.point_cloud:
            print("Opening 3D Viewer... Use mouse to rotate and see behind the camera.")
            o3d.visualization.draw_geometries([self.point_cloud], 
                                              window_name="AutoPoint 3D Scanner - 360 View",
                                              width=1200, height=800)

if __name__ == "__main__":
    # আপনার কম্পিউটারে থাকা E57 ফাইলের নাম এখানে দিন
    # উদাহরণ: scan_room.e57
    file_to_test = "sample.e57" 
    
    scanner = AutoPointScanner(file_to_test)
    if scanner.load_data():
        scanner.remove_nadir_mask()
        scanner.run_viewer()
