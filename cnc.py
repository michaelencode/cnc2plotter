import re


def modify_gcode(input_file, output_file):
    with open(input_file, 'r') as file:
        lines = file.readlines()

    with open(output_file, 'w') as file:
        for line in lines:
            # Convert G01 to G1
            if 'G01' in line or 'G00' in line:
                line = line.replace('G01', 'G0').replace('G00','G0')

            # Convert G02 and G03 to G1
            elif 'G02' in line or 'G03' in line:
                line = line.replace('G02', 'G1').replace('G03', 'G1')
            # Remove I and J with their values
            line = re.sub(r'I-?\d*\.?\d*', '', line)
            line = re.sub(r'J-?\d*\.?\d*', '', line)

            # Find Z value and add 10
            z_match = re.search(r'Z(-?\d+\.?\d*)', line)
            if z_match:
                z_value = float(z_match.group(1)) + 10
                line = re.sub(r'Z-?\d+\.?\d*', f'Z{z_value}', line)
            # Find Y value and reduce 10
            y_match = re.search(r'Y(-?\d+\.?\d*)', line)
            if y_match:
                y_value = float(y_match.group(1)) +140
                line = re.sub(r'Y-?\d+\.?\d*', f'Y{y_value}', line)

            x_match = re.search(r'X(-?\d+\.?\d*)', line)
            if x_match:
                x_value = float(x_match.group(1)) +40
                line = re.sub(r'X-?\d+\.?\d*', f'X{x_value}', line)

            # Scale down Y value by 50%
            y_match = re.search(r'Y(-?\d+\.?\d*)', line)
            if y_match:
                y_value = float(y_match.group(1)) * 0.22
                line = re.sub(r'Y-?\d+\.?\d*', f'Y{y_value}', line)

            # Scale down X value by 50%
            x_match = re.search(r'X(-?\d+\.?\d*)', line)
            if x_match:
                x_value = float(x_match.group(1)) * 0.22
                line = re.sub(r'X-?\d+\.?\d*', f'X{x_value}', line)



            # Modify F value to F1500
            line = re.sub(r'F\d+', 'F1500', line)
            file.write(line)


# Example usage
modify_gcode('cnccode.gcode', 'modified_gcode.gcode')
