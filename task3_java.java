import java.io.*;
import java.util.*;

class Student {
    private String name;
    private String rollNumber;
    private String grade;
    private int age;

    public Student(String name, String rollNumber, String grade, int age) {
        this.name = name;
        this.rollNumber = rollNumber;
        this.grade = grade;
        this.age = age;
    }

    public String getName() { return name; }
    public String getRollNumber() { return rollNumber; }
    public String getGrade() { return grade; }
    public int getAge() { return age; }

    public void setName(String name) { this.name = name; }
    public void setGrade(String grade) { this.grade = grade; }
    public void setAge(int age) { this.age = age; }

    @Override
    public String toString() {
        return rollNumber + "," + name + "," + grade + "," + age;
    }

    public static Student fromString(String line) {
        String[] parts = line.split(",");
        return new Student(parts[1], parts[0], parts[2], Integer.parseInt(parts[3]));
    }
}

public class StudentManagementSystem {
    private static final String FILE_NAME = "students.txt";
    private static List<Student> students = new ArrayList<>();
    private static Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {
        loadStudentsFromFile();

        while (true) {
            showMenu();
            String choice = scanner.nextLine();

            switch (choice) {
                case "1": addStudent(); break;
                case "2": editStudent(); break;
                case "3": searchStudent(); break;
                case "4": displayAllStudents(); break;
                case "5": removeStudent(); break;
                case "6":
                    saveStudentsToFile();
                    System.out.println("Exiting application.");
                    return;
                default: System.out.println("Invalid choice. Try again.");
            }
        }
    }

    private static void showMenu() {
        System.out.println("\nStudent Management System");
        System.out.println("1. Add Student");
        System.out.println("2. Edit Student");
        System.out.println("3. Search Student by Roll Number");
        System.out.println("4. Display All Students");
        System.out.println("5. Remove Student");
        System.out.println("6. Exit");
        System.out.print("Enter your choice: ");
    }

    private static void addStudent() {
        System.out.print("Enter Roll Number: ");
        String roll = scanner.nextLine().trim();
        if (roll.isEmpty()) {
            System.out.println("Roll number cannot be empty.");
            return;
        }
        if (getStudentByRoll(roll) != null) {
            System.out.println("Student with this roll number already exists.");
            return;
        }

        System.out.print("Enter Name: ");
        String name = scanner.nextLine().trim();
        if (name.isEmpty()) {
            System.out.println("Name cannot be empty.");
            return;
        }

        System.out.print("Enter Grade: ");
        String grade = scanner.nextLine().trim();
        if (grade.isEmpty()) {
            System.out.println("Grade cannot be empty.");
            return;
        }

        System.out.print("Enter Age: ");
        int age;
        try {
            age = Integer.parseInt(scanner.nextLine().trim());
            if (age <= 0) throw new NumberFormatException();
        } catch (NumberFormatException e) {
            System.out.println("Invalid age input.");
            return;
        }

        students.add(new Student(name, roll, grade, age));
        saveStudentsToFile();
        System.out.println("Student added successfully.");
    }

    private static void editStudent() {
        System.out.print("Enter Roll Number of student to edit: ");
        String roll = scanner.nextLine().trim();
        Student student = getStudentByRoll(roll);

        if (student == null) {
            System.out.println("Student not found.");
            return;
        }

        System.out.print("Enter new name (or press Enter to keep '" + student.getName() + "'): ");
        String name = scanner.nextLine().trim();
        if (!name.isEmpty()) student.setName(name);

        System.out.print("Enter new grade (or press Enter to keep '" + student.getGrade() + "'): ");
        String grade = scanner.nextLine().trim();
        if (!grade.isEmpty()) student.setGrade(grade);

        System.out.print("Enter new age (or press Enter to keep '" + student.getAge() + "'): ");
        String ageInput = scanner.nextLine().trim();
        if (!ageInput.isEmpty()) {
            try {
                int age = Integer.parseInt(ageInput);
                if (age > 0) student.setAge(age);
                else System.out.println("Invalid age input. Keeping previous value.");
            } catch (NumberFormatException e) {
                System.out.println("Invalid input. Age unchanged.");
            }
        }

        saveStudentsToFile();
        System.out.println("Student record updated.");
    }

    private static void searchStudent() {
        System.out.print("Enter Roll Number to search: ");
        String roll = scanner.nextLine().trim();
        Student student = getStudentByRoll(roll);

        if (student != null) {
            System.out.println("Student Found:");
            System.out.println("Roll Number: " + student.getRollNumber());
            System.out.println("Name: " + student.getName());
            System.out.println("Grade: " + student.getGrade());
            System.out.println("Age: " + student.getAge());
        } else {
            System.out.println("Student not found.");
        }
    }

    private static void displayAllStudents() {
        if (students.isEmpty()) {
            System.out.println("No student records found.");
            return;
        }

        System.out.println("\nAll Students:");
        for (Student s : students) {
            System.out.println("Roll Number: " + s.getRollNumber() + ", Name: " + s.getName() +
                               ", Grade: " + s.getGrade() + ", Age: " + s.getAge());
        }
    }

    private static void removeStudent() {
        System.out.print("Enter Roll Number of student to remove: ");
        String roll = scanner.nextLine().trim();
        Student student = getStudentByRoll(roll);

        if (student != null) {
            students.remove(student);
            saveStudentsToFile();
            System.out.println("Student removed.");
        } else {
            System.out.println("Student not found.");
        }
    }

    private static Student getStudentByRoll(String roll) {
        for (Student s : students) {
            if (s.getRollNumber().equalsIgnoreCase(roll)) return s;
        }
        return null;
    }

    private static void loadStudentsFromFile() {
        try (BufferedReader br = new BufferedReader(new FileReader(FILE_NAME))) {
            String line;
            while ((line = br.readLine()) != null) {
                students.add(Student.fromString(line));
            }
        } catch (IOException e) {
            // File may not exist on first run
        }
    }

    private static void saveStudentsToFile() {
        try (BufferedWriter bw = new BufferedWriter(new FileWriter(FILE_NAME))) {
            for (Student s : students) {
                bw.write(s.toString());
                bw.newLine();
            }
        } catch (IOException e) {
            System.out.println("Error saving student data.");
        }
    }
}
