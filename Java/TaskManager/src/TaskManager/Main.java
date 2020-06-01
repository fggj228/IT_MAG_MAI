package TaskManager;

import TaskManager.models.FileReader;
import TaskManager.models.Resolver;
import TaskManager.models.task.Task;
import TaskManager.models.task.TaskReader;

import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Random;

public class Main {
    public static final int ITERATIONS = 100;
    public static final String FILE_NAME = "tasks.txt";

    public static void main(String[] args) {
        new Main().mainFoo();
    }

    private void mainFoo(){
        final FileReader fileReader = new TaskReader();
        taskList = fileReader.read(FILE_NAME);
        //mock case
        task_resources = fileReader.getLastResources();
        for (int i=0; i<ITERATIONS; i++){
            new Solver();
        }
    }

    private List<Task> taskList;

    private List<Integer> task_resources;

    class Solver implements Runnable {
        private Thread thread;
        Solver() {
            thread = new Thread(this);
            thread.start();
        }

        public void run() {
            Random random = new Random(System.currentTimeMillis());
            HashSet<Integer> values = new HashSet();
            values.add(0);
            for (int j=0; j<10 +random.nextInt(taskList.size()-10); j++){
                values.add(Math.abs( random.nextInt() % taskList.size() ));
            }
            new Resolver(taskList, new ArrayList(values), task_resources).init();
        }
    }
}
