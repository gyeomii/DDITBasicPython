package application;

import javafx.application.Application;
import javafx.event.Event;
import javafx.event.EventHandler;
import javafx.fxml.FXMLLoader;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.TextField;
import javafx.stage.Stage;

public class Main3 extends Application {
	Parent root;
	Scene scene;
	Button btn;
	TextField tf1;
	TextField tf2;
	TextField tf3;
	@Override
	public void start(Stage primaryStage) {
		try {
			root = FXMLLoader.load(getClass().getResource("main3.fxml"));
			scene = new Scene(root, 800, 400); //(width, height)
			btn = (Button)scene.lookup("#btn");
			tf1 = (TextField)scene.lookup("#tf1");
			tf2 = (TextField)scene.lookup("#tf2");
			tf3 = (TextField)scene.lookup("#tf3");
			
			btn.setOnMouseClicked(new EventHandler<Event>() {
				@Override
				public void handle(Event event) {
					sum();
				}
			});
			scene.getStylesheets().add(getClass().getResource("application.css").toExternalForm());
			primaryStage.setScene(scene);
			primaryStage.show();
		} catch (Exception e) {
			e.printStackTrace();
		}
	}

	public void sum() {
		long n1 = Long.parseLong(tf1.getText());
		long n2 = Long.parseLong(tf2.getText());
		String txt = String.valueOf(n1 + n2); 
		tf3.setText(txt);
	}
	
	public static void main(String[] args) {
		launch(args);
	}
}
