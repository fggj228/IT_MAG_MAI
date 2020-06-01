package TaskManager.models.task;

import TaskManager.models.FileReader;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class TaskReader implements FileReader {
    private TaskConvert taskConverter = new TaskConvert();


    List<Integer> lastResources;

    @Override
    public List<Integer> getLastResources() {
        return lastResources;
    }

    @Override
    public List<Task> read(String filename) {
        try {
            File myObj = new File(filename );
            Scanner myReader = new Scanner(myObj);
            myReader.nextInt();
            List<Task> list = new ArrayList<Task>();

            int resourcesCount = myReader.nextInt();
            myReader.nextLine();
            lastResources = new ArrayList<Integer>();
            for (String data: myReader.nextLine().trim().split(" +") ){
                lastResources.add(Integer.parseInt(data));
            }
            while (myReader.hasNextLine()) {
                list.add(
                        taskConverter.convert(myReader.nextLine(), resourcesCount)
                );
            }
            myReader.close();
            return list;
        } catch (FileNotFoundException e) {
            System.out.println("An error occurred.");
            e.printStackTrace();
        }
        return null;
    }
}
