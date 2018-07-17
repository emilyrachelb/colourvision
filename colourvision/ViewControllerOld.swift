//
//  ViewController.swift
//  colourvision
//
//  Created by Samantha Emily-Rachel Belnavis on 2018-07-14.
//  Copyright © 2018 Samantha Emily-Rachel Belnavis. All rights reserved.
//

import UIKit
import AVKit
import Vision
import CoreML

class ViewController: UIViewController {
    // MARK: Properties
    @IBOutlet weak var imageView: UIImageView!
    @IBOutlet weak var confidenceLabel: UILabel!
    @IBOutlet weak var objectLabel: UILabel!
    
    override func viewDidLoad() {
        super.viewDidLoad()
    }
    
    override func viewDidAppear(_ animated: Bool){
        super.viewDidAppear(animated)
    }
}

extension ViewController: AVCaptureVideoDataOutputSampleBufferDelegate {
    func setupSession() {
        guard let device = AVCaptureDevice.default(for: .video) else { return }
        guard let input = try? AVCaptureDeviceInput(device: device) else { return }
        
        let session = AVCaptureSession()
        session.sessionPreset = .hd4K3840x2160
        
        let previewLayer = AVCaptureVideoPreviewLayer(session: session)
        previewLayer.frame = view.frame
        imageView.layer.addSublayer(previewLayer)
        
        let output = AVCaptureVideoDataOutput()
        output.setSampleBufferDelegate(self, queue: DispatchQueue(label: "videoQueue"))
        session.addOutput(output)
        
        session.addInput(input)
        session.startRunning()
    }
    
    func captureOutput(_ output: AVCaptureOutput, didOutput sampleBuffer: CMSampleBuffer, from connection: AVCaptureConnection) {
        guard let pixelBuffer: CVPixelBuffer = CMSampleBufferGetImageBuffer(sampleBuffer) else { return }
        guard let model = try? VNCoreMLModel(for: ColourModel().model) else { return }
        
        let request = VNCoreMLRequest(model: model) { [weak self] (data, error) in
            // check if the data is in the correct format, then assign to 'results'
            guard let results = data.results as? [VNClassificationObservation] else { return }
            
            // assign the first result (if it exists) to firstObject
            guard let firstObject = results.first else { return }
            
            if ((firstObject.confidence * 100) >= 50) {
                self?.objectLabel.text = firstObject.identifier.capitalized
                self?.confidenceLabel.text = String(firstObject.confidence * 100) + "%"
            }
        }
        
        let handler = VNImageRequestHandler(cvPixelBuffer: pixelBuffer, options: [:])
        do {
            try handler.perform([request])
        } catch {
            print("Failed to perform classification. \n \(error.localizedDescription)")
        }
    }
}
