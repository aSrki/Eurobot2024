from typing import Dict, List, Optional
import time
import matplotlib.pyplot as plt
from datetime import datetime
import os

class PIDPlotter:
    def __init__(self, should_plot_translation = True, should_plot_rotation = True):

        self.should_plot_translation = should_plot_translation
        self.should_plot_rotation = should_plot_rotation

        # Podatci za plotovanje
        self.plot_data = {
            'translation': {
                'time_translation': [],
                'x_location': [],
                'y_location': [],
                'des_location': [],
                'error': [],
                'filtered_error': [],
                'p_term': [],
                'i_term': [],
                'd_term': [],
                'output': []
            },
            'rotation': {
                'time_rotation': [],
                'error': [],
                'filtered_error': [],
                'p_term': [],
                'i_term': [],
                'd_term': [],
                'output': []
            },
            'motors': {
                'time_motors': [],
                'mvl': [],
                'mvr': []
            }
        }

        # Pocetno vreme pracenja
        self.start_time = time.time()


    def _log_plot_data(self, controller: str, values: Dict[str, float]):
        """Log data for plotting"""
        
        #print("Logging: " + controller + "\n")

        # Add timestamp for this data point 
        current_time = time.time() - self.start_time
        if(controller == 'translation'):
            # print("\n\nLOGGING TRANS")
            # print( "time: " + str(len(self.plot_data['translation']['time_translation'])))
            # print("translation: " + str(len(self.plot_data['translation']['des_location'])))
            self.plot_data['translation']['time_translation'].append(current_time)
        elif(controller == 'rotation'):
            self.plot_data['rotation']['time_rotation'].append(current_time)
            # print("LOGGING ROT")


        
        # Log controller-specific values
        for key, value in values.items():
            if key in self.plot_data[controller]:
                self.plot_data[controller][key].append(value)


    def _log_motor_data(self, mvl: float, mvr: float):
        """Log motor data for plotting"""
        
        current_time = time.time() - self.start_time
        
        self.plot_data['motors']['time_motors'].append(current_time)
            
        self.plot_data['motors']['mvl'].append(mvl)
        self.plot_data['motors']['mvr'].append(mvr)

## ----------------------------------------------------------------------------------- ##
##                                  PLOTING FUNKCIJE                                   ##
## ----------------------------------------------------------------------------------- ##


    def plot_translation(self, save: bool = True, folder: str = "TranlsationPlots"):
        """plotovanje (samo translacija trenutno)"""
        print("trying to plot---------------------------------------------")
        translation = self.plot_data['translation']
        time_vals = translation['time_translation']
        
        if not time_vals:
            print("No translation data available to plot.")
            return
        
        #plt.figure(figsize=(10, 6))
        
        fig, ax = plt.subplots(figsize=(10, 6))

        # Komentarisati trazene varijable
        ax.plot(time_vals, translation['des_location'], label='Desired Location', color='blue')
        ax.plot(time_vals, translation['error'], label='Error', color='red')
        ax.plot(time_vals, translation['filtered_error'], label='Filtered Error', color='green')
        # ax.plot(time_vals, translation['p_term'], label='P Term', color='cyan')
        # ax.plot(time_vals, translation['i_term'], label='I Term', color='magenta')
        # ax.plot(time_vals, translation['d_term'], label='D Term', color='orange')
        ax.plot(time_vals, translation['output'], label='Output', color='black')
        
        ax.set_xlabel("Time (s)")
        ax.set_ylabel("Value")
        ax.set_title("Translation PID Data")
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        #plt.show()

        if save:
            print("SAVING PLOTS!")
            try:
                # Use the "plots" directory as the base folder
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                base_folder = os.path.join(os.getcwd(), "plots", folder)
                os.makedirs(base_folder, exist_ok=True)
                
                filename = f"pid_debug_{timestamp}.png"
                save_path = os.path.join(base_folder, filename)
                
                # Save the figure
                fig.savefig(save_path, dpi=300, bbox_inches='tight')
                print(f"Plot saved to: {save_path}")
                plt.close(fig)
            except Exception as e:
                print(f"An error occurred while saving the plot: {e}")
        else:
            plt.show()

    def plot_rotation(self, save: bool = True, folder: str = "RotationPlots"):
        """Plot rotation PID data."""
        print("Generating rotation plot...")
        rotation = self.plot_data['rotation']
        time_vals = rotation['time_rotation']
        
        if not time_vals:
            print("No rotation data available to plot.")
            return
        
        fig, ax = plt.subplots(figsize=(10, 6))
        
        # Plot rotation data (you can add more signals if needed)
        ax.plot(time_vals, rotation['error'], label='Error', color='red')
        ax.plot(time_vals, rotation['filtered_error'], label='Filtered Error', color='green')
        # Optionally, plot P, I, D terms:
        # ax.plot(time_vals, rotation['p_term'], label='P Term', color='cyan')
        # ax.plot(time_vals, rotation['i_term'], label='I Term', color='magenta')
        # ax.plot(time_vals, rotation['d_term'], label='D Term', color='orange')
        ax.plot(time_vals, rotation['output'], label='Output', color='black')
        
        ax.set_xlabel("Time (s)")
        ax.set_ylabel("Value")
        ax.set_title("Rotation PID Data")
        ax.legend()
        ax.grid(True)
        plt.tight_layout()

        if save:
            print("Saving rotation plot...")
            try:
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                base_folder = os.path.join(os.getcwd(), "plots", folder)
                os.makedirs(base_folder, exist_ok=True)
                
                filename = f"pid_rotation_{timestamp}.png"
                save_path = os.path.join(base_folder, filename)
                fig.savefig(save_path, dpi=300, bbox_inches='tight')
                print(f"Rotation plot saved to: {save_path}")
                plt.close(fig)
            except Exception as e:
                print(f"An error occurred while saving the rotation plot: {e}")
        else:
            plt.show()

    def plot_motors(self, save: bool = True, folder: str = "MotorPlots"):
        """Plot motor speed data."""
        print("Generating motor speed plot...")
        motors = self.plot_data['motors']
        time_vals = motors['time_motors']
        
        if not time_vals:
            print("No motor data available to plot.")
            return
        
        fig, ax = plt.subplots(figsize=(10, 6))
        
        ax.plot(time_vals, motors['mvl'], label='Left Motor', color='blue')
        ax.plot(time_vals, motors['mvr'], label='Right Motor', color='red')
        
        ax.set_xlabel("Time (s)")
        ax.set_ylabel("Motor Speed")
        ax.set_title("Motor Speed Data")
        ax.legend()
        ax.grid(True)
        plt.tight_layout()

        if save:
            print("Saving motor speed plot...")
            try:
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                base_folder = os.path.join(os.getcwd(), "plots", folder)
                os.makedirs(base_folder, exist_ok=True)
                
                filename = f"pid_motors_{timestamp}.png"
                save_path = os.path.join(base_folder, filename)
                fig.savefig(save_path, dpi=300, bbox_inches='tight')
                print(f"Motor plot saved to: {save_path}")
                plt.close(fig)
            except Exception as e:
                print(f"An error occurred while saving the motor plot: {e}")
        else:
            plt.show()


    def plot_all(self, save: bool = True, folder: str = "CombinedPlots"):
        """
        Plot everything combined in a 2x2 grid:
         - Top-left: Translation PID data.
         - Top-right: Rotation PID data.
         - Bottom-left: Motor speed data.
         - Bottom-right: Left empty.
        """
        print("Generating combined plot...")
        fig, axs = plt.subplots(2, 2, figsize=(15, 10))
        
        # --- Translation Plot (Top-Left) ---
        translation = self.plot_data['translation']
        t_time = translation['time_translation']
        if t_time:
            axs[0, 0].plot(t_time, translation['des_location'], label='Desired Location', color='blue')
            axs[0, 0].plot(t_time, translation['error'], label='Error', color='red')
            axs[0, 0].plot(t_time, translation['filtered_error'], label='Filtered Error', color='green')
            axs[0, 0].plot(t_time, translation['output'], label='Output', color='black')
            axs[0, 0].set_xlabel("Time (s)")
            axs[0, 0].set_ylabel("Value")
            axs[0, 0].set_title("Translation PID Data")
            axs[0, 0].legend()
            axs[0, 0].grid(True)

            axs[1, 1].plot(t_time, translation['x_location'], label='Current X', color='blue')
            axs[1, 1].plot(t_time, translation['y_location'], label='Current Y', color='red')
            axs[1, 1].set_xlabel("Time (s)")
            axs[1, 1].set_ylabel("Value")
            axs[1, 1].set_title("XY Data")
            axs[1, 1].legend()
            axs[1, 1].grid(True)

        else:
            axs[0, 0].text(0.5, 0.5, "No translation data available", ha='center', va='center')
            axs[0, 0].set_title("Translation PID Data")
            axs[0, 0].axis('off')

            axs[1, 1].text(0.5, 0.5, "No translation data available", ha='center', va='center')
            axs[1, 1].set_title("Translation PID Data")
            axs[1, 1].axis('off')
        
        # --- Rotation Plot (Top-Right) ---
        rotation = self.plot_data['rotation']
        r_time = rotation['time_rotation']
        if r_time:
            axs[0, 1].plot(r_time, rotation['error'], label='Error', color='red')
            axs[0, 1].plot(r_time, rotation['filtered_error'], label='Filtered Error', color='green')
            axs[0, 1].plot(r_time, rotation['output'], label='Output', color='black')
            axs[0, 1].set_xlabel("Time (s)")
            axs[0, 1].set_ylabel("Value")
            axs[0, 1].set_title("Rotation PID Data")
            axs[0, 1].legend()
            axs[0, 1].grid(True)
        else:
            axs[0, 1].text(0.5, 0.5, "No rotation data available", ha='center', va='center')
            axs[0, 1].set_title("Rotation PID Data")
            axs[0, 1].axis('off')
        
        # --- Motor Speed Plot (Bottom-Left) ---
        motors = self.plot_data['motors']
        m_time = motors['time_motors']
        if m_time:
            axs[1, 0].plot(m_time, motors['mvl'], label='Left Motor', color='blue')
            axs[1, 0].plot(m_time, motors['mvr'], label='Right Motor', color='red')
            axs[1, 0].set_xlabel("Time (s)")
            axs[1, 0].set_ylabel("Motor Speed")
            axs[1, 0].set_title("Motor Speed Data")
            axs[1, 0].legend()
            axs[1, 0].grid(True)
        else:
            axs[1, 0].text(0.5, 0.5, "No motor data available", ha='center', va='center')
            axs[1, 0].set_title("Motor Speed Data")
            axs[1, 0].axis('off')

        
        
        # --- Fourth Subplot (Bottom-Right): Left Empty ---
        axs[1, 1].axis('off')

        plt.tight_layout()

        if save:
            print("Saving combined plot...")
            try:
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                base_folder = os.path.join(os.getcwd(), "plots", folder)
                os.makedirs(base_folder, exist_ok=True)
                
                filename = f"pid_combined_{timestamp}.png"
                save_path = os.path.join(base_folder, filename)
                fig.savefig(save_path, dpi=300, bbox_inches='tight')
                print(f"Combined plot saved to: {save_path}")
                plt.close(fig)
            except Exception as e:
                print(f"An error occurred while saving the combined plot: {e}")
        else:
            plt.show()