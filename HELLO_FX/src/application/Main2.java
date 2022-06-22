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

public class Main2 extends Application {
	Parent root;
	Scene scene;
	Button btn;
	TextField tf;
	@Override
	public void start(Stage primaryStage) {
		try {
			root = FXMLLoader.load(getClass().getResource("main2.fxml"));
			scene = new Scene(root, 400, 400);
			btn = (Button)scene.lookup("#btn");
			tf = (TextField)scene.lookup("#tf");
			btn.setOnMouseClicked(new EventHandler<Event>() {
				@Override
				public void handle(Event event) {
					plusOne();
				}
			});
			scene.getStylesheets().add(getClass().getResource("application.css").toExternalForm());
			primaryStage.setScene(scene);
			primaryStage.show();
		} catch (Exception e) {
			e.printStackTrace();
		}
	}

	public void plusOne() {
		int n = Integer.parseInt(tf.getText());
		String txt = String.valueOf(++n);
		tf.setText(txt);
	}
	
	public static void main(String[] args) {
		launch(args);
	}
}
